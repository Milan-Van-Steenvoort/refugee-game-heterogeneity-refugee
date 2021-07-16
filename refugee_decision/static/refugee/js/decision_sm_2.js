/* Refugee game decision calculations */


/*********************************/ 
/*FOR SECOND MOVERS: decision 2 */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_2 = document.getElementById("sliderRange_2"); 
var output_sm_2 = document.getElementById("decision_sm_2");
var output2_sm_2 = document.getElementById("personal_share_sm_2");
var output3_sm_2 = document.getElementById("citizen_share_sm_2");
var output4_sm_2 = document.getElementById("refugee_share_sm_2");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
rangeslider_2.onclick = function() {
	rangeslider_2.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    

/*At first sight, this just defines initial values for the output variables. */
output_sm_2.innerHTML = " "; 
output2_sm_2.innerHTML = (25).toFixed(2);
output3_sm_2.innerHTML = (25).toFixed(2);
output4_sm_2.innerHTML = (0).toFixed(2);        

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_2.oninput = function() {
	rangeslider_2.className = "clicked";	
	output_sm_2.innerHTML = this.value;
	output2_sm_2.innerHTML = ((100 - this.value)/4).toFixed(2);
	output3_sm_2.innerHTML = output2_sm_2.innerHTML;
	output4_sm_2.innerHTML = (this.value*1).toFixed(2);
}