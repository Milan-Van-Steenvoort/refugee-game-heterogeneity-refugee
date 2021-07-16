/* Refugee game decision calculations */


/*********************************/ 
/*FOR REFUGEE BELIEF: ref_belief_sim_hh_A */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_01 = document.getElementById("sliderRange_01"); 
var output_ref_01 = document.getElementById("ref_belief_sim_hh_A");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
/*rangeslider_01.onclick = function() {
	rangeslider_01.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}  */

/*At first sight, this just defines initial values for the output variables. */
output_ref_01.innerHTML = " "; 
      

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_01.oninput = function() {
	rangeslider_01.className = "clicked";	
	output_ref_01.innerHTML = this.value;
}

/*********************************/ 
/*FOR REFUGEE BELIEF: ref_belief_sim_hh_B */
/********************************/


/*At first sight, this just defines output variables. Their value is defined below */
var rangeslider_02 = document.getElementById("sliderRange_02"); 
var output_ref_02 = document.getElementById("ref_belief_sim_hh_B");
var confirm_button = document.getElementById("button_id");

/*At first sight, this means that the button Next only gets activated when the rangerslider has been moved */
rangeslider_02.onclick = function() {
	rangeslider_02.className = "clicked";
	confirm_button.disabled = false;
	confirm_button.innerHTML = "Next";
}    

/*At first sight, this just defines initial values for the output variables. */
output_ref_02.innerHTML = " "; 
      

/*At first sight, this  defines the function generating the values for the output variables. */
rangeslider_02.oninput = function() {
	rangeslider_02.className = "clicked";	
	output_ref_02.innerHTML = this.value;
}




