$(function(){
	$('button').click(function(){
		var address = $('#address-input').val();
		$.ajax({
			url: '/doStuff',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				var obj = JSON.parse(response);
				alert('Your roof size is ' + obj.roof);
				document.getElementById("roof-input").value = 'Your address is ' + obj.address + ' and your bill is ' + obj.bill;
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
