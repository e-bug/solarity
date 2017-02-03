$("#address-text").keypress(function(event){
    if(event.keyCode == 13){
        event.preventDefault();
        $("#address-button").click();
    }
});

$("#bill-input").keypress(function(event){
    if(event.keyCode == 13){
        event.preventDefault();
        $("#ready-but").click();
    }
});
$("#roof-input").keypress(function(event){
    if(event.keyCode == 13){
        event.preventDefault();
        $("#ready-but").click();
    }
});

function updateBillVal(val) {
    document.getElementById('bill-out').value = val; 
}
function updateRoofVal(val) {
    document.getElementById('roof-out').value = val; 
}

