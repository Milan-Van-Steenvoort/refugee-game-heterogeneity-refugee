/* Refugee game decision calculations */


/*******************************************************/ 
/*FOR FIRST MOVERS AND SIMULTANEOUS: only one decision */
/******************************************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider = document.getElementById("sliderRange"); 
var output = document.getElementById("decision");
var output2 = document.getElementById("personal_share");
var output3 = document.getElementById("citizen_share");
var output4 = document.getElementById("refugee_share");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
rangeslider.onclick = function() {
	rangeslider.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    

/*At first sight, this just defines initial values for the output variables. */
output.innerHTML = " "; 
output2.innerHTML = (25).toFixed(2);
output3.innerHTML = (25).toFixed(2);
output4.innerHTML = (0).toFixed(2);        

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider.oninput = function() {
	rangeslider.className = "clicked";	
	output.innerHTML = this.value;
	output2.innerHTML = ((100 - this.value)/4).toFixed(2);
	output3.innerHTML = output2.innerHTML;
	output4.innerHTML = (this.value*1).toFixed(2);
}







