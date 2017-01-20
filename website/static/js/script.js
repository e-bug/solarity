function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                alert(allText);
            }
        }
    }
    rawFile.send(null);
}

// $(document).ready(function(){
//     $('#address-text').keypress(function(e){
//       if(e.keyCode == 13)
//       $('#address-button').click();
//     });
// });

$("#address-text").keypress(function(event){
    if(event.keyCode == 13){
        event.preventDefault();
        $("#address-button").click();
    }
});