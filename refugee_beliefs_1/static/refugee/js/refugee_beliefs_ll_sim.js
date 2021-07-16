/*********************************/ 
/*FOR REFUGEE BELIEF: ref_belief_sim_ll_A */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_05 = document.getElementById("sliderRange_05"); 
var output_ref_05 = document.getElementById("ref_belief_sim_ll_A");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
/*rangeslider_05.onclick = function() {
	rangeslider_05.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    */

/*At first sight, this just defines initial values for the output variables. */
output_ref_05.innerHTML = " "; 
      

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_05.oninput = function() {
	rangeslider_05.className = "clicked";	
	output_ref_05.innerHTML = this.value;
}

/*********************************/ 
/*FOR REFUGEE BELIEF: ref_belief_sim_ll_B */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_06 = document.getElementById("sliderRange_06"); 
var output_ref_06 = document.getElementById("ref_belief_sim_ll_B");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
rangeslider_06.onclick = function() {
	rangeslider_06.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    

/*At first sight, this just defines initial values for the output variables. */
output_ref_06.innerHTML = " "; 
      

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_06.oninput = function() {
	rangeslider_06.className = "clicked";	
	output_ref_06.innerHTML = this.value;
}