/* Refugee game decision calculations */

var rangeslider = document.getElementById("sliderRange2"); 
var confirm_button = document.getElementById("button_id");

rangeslider.onclick = function() {
	rangeslider.className = "clicked";
	confirm_button.disabled = false;
}

var output = document.getElementById("belief");
output.innerHTML = " "; 

rangeslider.oninput = function() { 
	output.innerHTML = this.value;
}