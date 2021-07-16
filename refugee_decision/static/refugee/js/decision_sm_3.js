/* Refugee game decision calculations */


/*********************************/ 
/*FOR SECOND MOVERS: decision 3 */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_3 = document.getElementById("sliderRange_3"); 
var output_sm_3 = document.getElementById("decision_sm_3");
var output2_sm_3 = document.getElementById("personal_share_sm_3");
var output3_sm_3 = document.getElementById("citizen_share_sm_3");
var output4_sm_3 = document.getElementById("refugee_share_sm_3");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
rangeslider_3.onclick = function() {
	rangeslider_3.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    

/*At first sight, this just defines initial values for the output variables. */
output_sm_3.innerHTML = " "; 
output2_sm_3.innerHTML = (25).toFixed(2);
output3_sm_3.innerHTML = (25).toFixed(2);
output4_sm_3.innerHTML = (0).toFixed(2);        

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_3.oninput = function() {
	rangeslider_3.className = "clicked";	
	output_sm_3.innerHTML = this.value;
	output2_sm_3.innerHTML = ((100 - this.value)/4).toFixed(2);
	output3_sm_3.innerHTML = output2_sm_3.innerHTML;
	output4_sm_3.innerHTML = (this.value*1).toFixed(2);
}