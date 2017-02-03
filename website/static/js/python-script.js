var obj;

/******************************** MAP HANDLING ********************************/

/* MARKER ICONS */
// possible colors: 'red', 'darkred', 'orange', 'green', 'darkgreen', 'blue', 'purple', 'darkpurple', 'cadetblue'

/* Marker icon for home position */
var homeIcon = L.AwesomeMarkers.icon({
					      prefix: 'fa',        // font awesome rather than bootstrap
					      markerColor: 'blue', // see colors above
					      icon: 'home'         // http://fortawesome.github.io/Font-Awesome/icons/
							});
/* Marker icon for weather stations */
var sunIcon = L.AwesomeMarkers.icon({
				        prefix: 'fa',          // font awesome rather than bootstrap
				        markerColor: 'purple', // see colors above
				        icon: 'sun-o'          // http://fortawesome.github.io/Font-Awesome/icons/
			    		});


/* MAP TILES */
var cartoDB = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
            		attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
         			});


/* INTIAL MAP */
var map = L.map('jumbo-img').setView([46.776043, 8.467892], 8);
cartoDB.addTo(map);


/* UPDATE MAP */
/* Function to update the map once an address is entered */
$(function(){
	$('#address-button').click(function(){
		$.ajax({
			url: '/getMap',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				
				obj = JSON.parse(response);

				if(Object.keys(obj).length == 0) alert("Address is invalid!");
				else
				{
					map.eachLayer(function (layer) {
			    	map.removeLayer(layer);
					});

					// add house to map
					var house = obj.house;
					
					map.setView([house.latitude, house.longitude], 11);
		
					var homeMarker = L.marker([house.latitude, house.longitude], {icon: homeIcon});
					var houseLat = parseFloat(Math.round(house.latitude * 100) / 100).toFixed(2);
					var houseLng =  parseFloat(Math.round(house.longitude * 100) / 100).toFixed(2);
					homeMarker.bindPopup("<b>Home</b>" + "<br>" + "(" + houseLat + "," + houseLng + ")");

					cartoDB.addTo(map);
					homeMarker.addTo(map);

					// add stations to map
					for (var key in obj) {
						if (obj[key].type == 'station') {
							var name = obj[key].name; 
							var lat =  parseFloat(Math.round(obj[key].latitude * 100) / 100).toFixed(2);
							var lng =  parseFloat(Math.round(obj[key].longitude * 100) / 100).toFixed(2);
							L.marker([lat, lng], {icon: sunIcon}).bindPopup("<b>" + name + "</b>" + "<br>" + "(" + lat + "," + lng + ")").addTo(map);
						}
					}

				}
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});


/****************************** CHARTS HANDLING ******************************/
var chart;
var bar;

/* Function to update the barplot once address, roof area and electric bill are entered */
$(function(){
	$('#ready-but').click(function(){
		$.ajax({
			url: '/doStuff',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				
				var bill = document.getElementById('bill-input').value
				var roof = document.getElementById('roof-input').value
				if(bill == 0 || roof == 0)
				{
					alert("Please enter you bill and roof size!");
					return;
				}

				document.getElementById('output').style.display = "block";

				obj = JSON.parse(response);
				if(Object.keys(obj).length == 0) alert("Address is invalid!");
				else
				{
					document.getElementById("roof-input").disabled = false;
					document.getElementById("bill-input").disabled = false;

					// Generate barplot
					var barData = [];
					for (var key in obj) {
						if (obj[key].type == 'result') {
							var percentage = obj[key].percentage; 
							var cost = obj[key].cost;
							var savings =  obj[key].savings;
							var entry = {'percentage': percentage, 'cost': cost, 'savings': savings};
							barData.push(entry);
						}
					}
					barData.sort(function(a, b){return a.percentage-b.percentage});

					bar = AmCharts.makeChart("bardiv", {
						"type": "serial",
					  "theme": "light",
						"categoryField": "percentage",
						"rotate": true,
						"startDuration": 1,
						"legend": {
			    		"enabled": true,
			        "useGraphSettings": true
				    },
						"categoryAxis": {
							"gridPosition": "start",
							"position": "left"
						},
						"trendLines": [],
						"graphs": [
							{
								"balloonText": "Initial Investment: [[value]] CHF",
								"fillAlphas": 0.8,
								"id": "AmGraph-1",
								"lineAlpha": 0.2,
								"fillColors": "#e30303",
								"title": "Initial Investment",
								"type": "column",
								"valueField": "cost"
							},
							{
								"balloonText": "Savings after 25 years: [[value]] CHF",
								"fillAlphas": 0.8,
								"id": "AmGraph-2",
								"lineAlpha": 0.2,
								"fillColors": "#03e303",
								"title": "Savings after 25 years",
								"type": "column",
								"valueField": "savings"
							}
						],
						"guides": [],
						"valueAxes": [
							{
								"id": "ValueAxis-1",
								"position": "top",
								"axisAlpha": 0,
								"title": "Amount [CHF]",
								"titleFontSize": 16
							}
						],
						"categoryAxis": {
							"title": "Percentage of roof covered",
							"titleFontSize": 16,
							"labelFunction": function(number, label, categoryAxis) {
     						 label = AmCharts.formatDataContextValue("[[value]] %", {
     						 		value: number
     						 	});

     						 return label;
    					}
						},
						"allLabels": [],
						"balloon": {},
						"titles": [],
						"dataProvider": barData,
					  "export": {
				    	"enabled": true,
				    	"position": "bottom-right"
				     }
					});

					drawGraph(5);
				}
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});


/* Function to update the chart once address, roof area and electric bill are entered */
function drawGraph(percentage) {

	var indexString = 'result_' + percentage.toString();
	if(obj[indexString] == undefined)
	{
		if(parseInt(percentage) == 0) alert("At least cover some of your roof with panels!");
		else alert("It wouldn't make sense to cover this much of your roof with panels. Try a smaller percentage!");
		return;
	}

	document.getElementById('payback-out').innerHTML = obj[indexString].breakEven;

	var chartData = generateChartData(obj[indexString].cost, obj[indexString].breakEven);
	chart = AmCharts.makeChart("chartdiv", {
	    "type": "serial",
	    "theme": "light",
	    "legend": {
    		"enabled": false,
        "useGraphSettings": true
	    },
	    "dataProvider": chartData,
	    "dataDateFormat": "YYYY-MM-DD",
	    "synchronizeGrid":true,
	    "valueAxes": [{
	        "id":"v1",
	        "axisAlpha": 1,
	        "position": "left",
	    }],
	    "graphs": [{
	        "valueAxis": "v1",
	        "lineColor": "#03e303",
	        "lineThickness": 2,
	        "negativeLineColor": "#e30303",
	        "bullet": "round",
	        "bulletBorderThickness": 1,
	        "hideBulletsCount": 30,
	        "title": "Savings [CHF]",
	        "valueField": "saving",
					"fillAlphas": 0
	    }],
	    "chartScrollbar": {},
	    "chartCursor": {
	        "cursorPosition": "mouse"
	    },
	    "categoryField": "date",
	    "categoryAxis": {
	        "parseDates": true,
	        "axisColor": "#DADADA",
	        "minorGridEnabled": true
	    },
	    "export": {
	        "enabled": true,
	        "position": "bottom-right"
	     },
	    "titles": [
		    {
		    	"text": "Annual savings when " + percentage + "% of roof is covered",
		    	"size": 18
		    }
	    ],
	});

	chart.addListener("dataUpdated", zoomChart);
	zoomChart();
}

/* Helper functions for chart*/
function zoomChart() {
	chart.zoomToIndexes(0, chart.dataProvider.length - 1);
}

function generateChartData(cost, breakEven) {
    var chartData = [];
    var savings = -parseInt(cost);
    var slope = parseInt(cost) / parseInt(breakEven);

    var breakYear = 2017 + parseInt(breakEven);
    var breakMonth = parseInt((breakEven - parseInt(breakEven)) * 12) + 1;
    var xaxis = breakYear.toString() + '-' + breakMonth.toString() + '-01';
    chartData.push({date: '2017-01-01', saving: savings});

    for (var i = 2018; i <= breakYear; i++) {

        savings = savings + slope
        var xaxis = i.toString() + '-01-01';

        chartData.push({
            date: xaxis,
            saving: savings
        });
    }

    chartData.push({date: xaxis, saving: 0});

    for (var i = breakYear + 1; i <= 2017 + 25; i++) {

        savings = savings + slope
        var xaxis = i.toString() + '-01-01';

        chartData.push({
            date: xaxis,
            saving: savings
        });
    }

    return chartData;
}
