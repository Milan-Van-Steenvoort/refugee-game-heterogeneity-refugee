/* Refugee game decision calculations */


/*********************************/ 
/*FOR SECOND MOVERS: decision 1 */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_1 = document.getElementById("sliderRange_1"); 
var output_sm_1 = document.getElementById("decision_sm_1");
var output2_sm_1 = document.getElementById("personal_share_sm_1");
var output3_sm_1 = document.getElementById("citizen_share_sm_1");
var output4_sm_1 = document.getElementById("refugee_share_sm_1");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
rangeslider_1.onclick = function() {
	rangeslider_1.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    

/*At first sight, this just defines initial values for the output variables. */
output_sm_1.innerHTML = " "; 
output2_sm_1.innerHTML = (25).toFixed(2);
output3_sm_1.innerHTML = (25).toFixed(2);
output4_sm_1.innerHTML = (0).toFixed(2);        

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_1.oninput = function() {
	rangeslider_1.className = "clicked";	
	output_sm_1.innerHTML = this.value;
	output2_sm_1.innerHTML = ((100 - this.value)/4).toFixed(2);
	output3_sm_1.innerHTML = output2_sm_1.innerHTML;
	output4_sm_1.innerHTML = (this.value*1).toFixed(2);
}

