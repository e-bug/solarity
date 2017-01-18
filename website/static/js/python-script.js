$(function(){
	$('button').click(function(){
		var address = $('#address-input').val();
		$.ajax({
			url: '/doStuff',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				var obj = JSON.parse(response);
				//document.getElementById("roof-input").value = 'Your address is ' + obj.address + ' and your bill is ' + obj.bill;
				if(obj.latitude == 0 && obj.longtitude == 0) alert("Address is invalid!");
				else
				{
					var map = L.map('jumbo-img').setView([obj.latitude, obj.longtitude], 15);

		            L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		                  maxZoom: 40,
		                  attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
		          	}).addTo(map);
		        }
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
