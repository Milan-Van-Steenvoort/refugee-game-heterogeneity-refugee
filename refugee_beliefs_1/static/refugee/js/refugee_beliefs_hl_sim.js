/*********************************/ 
/*FOR REFUGEE BELIEF: ref_belief_sim_hl_A */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_03 = document.getElementById("sliderRange_03"); 
var output_ref_03 = document.getElementById("ref_belief_sim_hl_A");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
/*rangeslider_03.onclick = function() {
	rangeslider_03.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    */

/*At first sight, this just defines initial values for the output variables. */
output_ref_03.innerHTML = " "; 
      

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_03.oninput = function() {
	rangeslider_03.className = "clicked";	
	output_ref_03.innerHTML = this.value;
}

/*********************************/ 
/*FOR REFUGEE BELIEF: ref_belief_sim_hl_B */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_04 = document.getElementById("sliderRange_04"); 
var output_ref_04 = document.getElementById("ref_belief_sim_hl_B");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
rangeslider_04.onclick = function() {
	rangeslider_04.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    

/*At first sight, this just defines initial values for the output variables. */
output_ref_04.innerHTML = " "; 
      

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_04.oninput = function() {
	rangeslider_04.className = "clicked";	
	output_ref_04.innerHTML = this.value;
}