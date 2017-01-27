var chart;
var bar;

/* Initial map */
var map = L.map('jumbo-img').setView([46.776043, 8.467892], 8);
var sunIcon = L.AwesomeMarkers.icon({
					        prefix: 'fa', //font awesome rather than bootstrap
					        markerColor: 'purple', // see colors above
					        icon: 'sun-o' //http://fortawesome.github.io/Font-Awesome/icons/
			    		});
var cartoDB = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
         });
cartoDB.addTo(map);


// function readTextFile(file)
// {
//     var rawFile = new XMLHttpRequest();
//     rawFile.open("GET", file, false);
//     rawFile.onreadystatechange = function ()
//     {
//         if(rawFile.readyState === 4)
//         {
//             if(rawFile.status === 200 || rawFile.status == 0)
//             {
//                 var allText = rawFile.responseText;
//                 alert(allText);
//             }
//         }
//     }
//     rawFile.send(null);
// }
// readTextFile('/stations_name_latlng_dict.json')

// var allStats = $.getJSON("stations_name_latlng_dict.json", function(json) {
//     console.log(json); // this will show the info it in firebug console
// });
// console.log(allStats);

// var geojsonCH = {"type":"Feature","id":"CHE","properties":{"name":"Switzerland"},"geometry":{"type":"Polygon","coordinates":[[[9.594226,47.525058],[9.632932,47.347601],[9.47997,47.10281],[9.932448,46.920728],[10.442701,46.893546],[10.363378,46.483571],[9.922837,46.314899],[9.182882,46.440215],[8.966306,46.036932],[8.489952,46.005151],[8.31663,46.163642],[7.755992,45.82449],[7.273851,45.776948],[6.843593,45.991147],[6.5001,46.429673],[6.022609,46.27299],[6.037389,46.725779],[6.768714,47.287708],[6.736571,47.541801],[7.192202,47.449766],[7.466759,47.620582],[8.317301,47.61358],[8.522612,47.830828],[9.594226,47.525058]]]}}
// L.geoJson(geojsonCH).addTo(map);
var obj;

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

					var house = obj.house;
					
					map.setView([house.latitude, house.longitude], 11);

					//possible colors 'red', 'darkred', 'orange', 'green', 'darkgreen', 'blue', 'purple', 'darkpurple', 'cadetblue'
					var homeIcon = L.AwesomeMarkers.icon({
					        prefix: 'fa', //font awesome rather than bootstrap
					        markerColor: 'blue', // see colors above
					        icon: 'home' //http://fortawesome.github.io/Font-Awesome/icons/
			    		});
					var homeMarker = L.marker([house.latitude, house.longitude], {icon: homeIcon});
					var houseLat = parseFloat(Math.round(house.latitude * 100) / 100).toFixed(2);
					var houseLng =  parseFloat(Math.round(house.longitude * 100) / 100).toFixed(2);
					homeMarker.bindPopup("<b>Home</b>" + "<br>" + "(" + houseLat + "," + houseLng + ")");

					var sunIcon = L.AwesomeMarkers.icon({
					        prefix: 'fa', //font awesome rather than bootstrap
					        markerColor: 'purple', // see colors above
					        icon: 'sun-o' //http://fortawesome.github.io/Font-Awesome/icons/
			    		});

					/* Some tiles */
					var OpenStreetMap_Mapnik = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
									maxZoom: 19,
									attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
							});
					var OpenCycleMap = L.tileLayer('http://{s}.tile.opencyclemap.org/cycle/{z}/{x}/{y}.png', {
									maxZoom: 19,
							});
					var Hydda_Full = L.tileLayer('http://{s}.tile.openstreetmap.se/hydda/full/{z}/{x}/{y}.png', {
									attribution: 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
							});
					var Stamen_TonerLite = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.{ext}', {
									attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
									subdomains: 'abcd',
									minZoom: 0,
									maxZoom: 20,
									ext: 'png'
							});
					var Stamen_Watercolor = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}', {
									attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
									subdomains: 'abcd',
									minZoom: 1,
									maxZoom: 16,
									ext: 'png'
							});
					var Stamen_Terrain = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.{ext}', {
									attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
									subdomains: 'abcd',
									minZoom: 0,
									maxZoom: 18,
									ext: 'png'
							});
      	 var cartoDB = L.tileLayer('http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
         });


					cartoDB.addTo(map);
					homeMarker.addTo(map);

					for (var key in obj) {
						if (obj[key].type == 'station') {
							var name = obj[key].name; 
							var lat =  parseFloat(Math.round(obj[key].latitude * 100) / 100).toFixed(2);
							var lng =  parseFloat(Math.round(obj[key].longitude * 100) / 100).toFixed(2);
							L.marker([lat, lng], {icon: sunIcon}).bindPopup("<b>" + name + "</b>" + "<br>" + "(" + lat + "," + lng + ")").addTo(map);
						}
						// else if(obj[key].type == 'result') {
						// 	console.log('percentage: ' + obj[key].percentage + '%')
						// 	console.log('cost: ' + obj[key].cost + ' CHF')
						// 	console.log('break even: ' + obj[key].breakEven + ' years')
						// 	console.log('capacity: ' + obj[key].capacity + ' kWp')
						// 	console.log('power: ' + obj[key].power + ' kW')
						// }
					}

				}
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});


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
				//document.getElementById("roof-input").value = 'Your address is ' + obj.address + ' and your bill is ' + obj.bill;
				if(Object.keys(obj).length == 0) alert("Address is invalid!");
				else
				{
					document.getElementById("roof-input").disabled = false;
					document.getElementById("bill-input").disabled = false;



					var barData = [];
					for (var key in obj) {
						if (obj[key].type == 'result') {
							var percentage = obj[key].percentage; 
							var cost = obj[key].cost;
							var savings =  obj[key].savings;
							var entry = {'percentage': percentage, 'cost': cost, 'savings': savings};
							barData.push(entry);

							// document.getElementById('payback-out').value = obj[key].breakEven; 
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
								"balloonText": "Initial investment: [[value]] CHF",
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

function drawGraph(percentage) {

	var indexString = 'result_' + percentage.toString();
	if(obj[indexString] == undefined)
	{
		if(parseInt(percentage) == 0) alert("At least cover some of your roof with panels!");
		else alert("It wouldn't make sense to cover this much of your roof with panels. Try a smaller percentage!");
		return;
	}

	document.getElementById('payback-out').value = obj[indexString].breakEven;

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
	        // "axisColor": "#FF6600",
	        // "axisThickness": 2,
	        "axisAlpha": 1,
	        "position": "left",
	        // "minimum":-10000,
	        // "maximum":10000
	    }],
	    "graphs": [{
	        "valueAxis": "v1",
	        // "lineColor": "#FF6600",
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
