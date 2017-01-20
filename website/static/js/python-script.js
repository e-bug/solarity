$(function(){
	$('#address-button').click(function(){
		var address = $('#address-input').val();
		$.ajax({
			url: '/doStuff',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				var obj = JSON.parse(response);
				//document.getElementById("roof-input").value = 'Your address is ' + obj.address + ' and your bill is ' + obj.bill;
				if(Object.keys(obj).length == 0) alert("Address is invalid!");
				// if(obj.latitude == 0 && obj.longtitude == 0) alert("Address is invalid!");
				else
				{
					house = obj.house
					var map = L.map('jumbo-img').setView([house.latitude, house.longtitude], 11);

					//possible colors 'red', 'darkred', 'orange', 'green', 'darkgreen', 'blue', 'purple', 'darkpurple', 'cadetblue'
			    var homeIcon = L.AwesomeMarkers.icon({
					        prefix: 'fa', //font awesome rather than bootstrap
					        markerColor: 'blue', // see colors above
					        icon: 'home' //http://fortawesome.github.io/Font-Awesome/icons/
			    		});
					var homeMarker = L.marker([house.latitude, house.longtitude], {
									icon: homeIcon
							});

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


					Stamen_Watercolor.addTo(map);
					homeMarker.addTo(map);

					for (var key in obj) {
						if (typeof(obj[key].name) != 'undefined') {
							// console.log([obj[key].name, obj[key].latitude, obj[key].longitude])
							L.marker([obj[key].latitude, obj[key].longitude], {
									icon: sunIcon
							}).addTo(map);
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
