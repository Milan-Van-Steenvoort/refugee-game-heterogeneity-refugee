/* Refugee game decision calculations */

var rangeslider1 = document.getElementById("sliderRange21");
var rangeslider2 = document.getElementById("sliderRange22");  
var confirm_button = document.getElementById("button_id");
var check1 = 0;
var check2 = 0;

rangeslider1.onclick = function() {
	if (check1 == 0) {
		check1 = 1}; 
	rangeslider1.className = "clicked";
	if (check1 == 1 & check2 == 1) {
		confirm_button.disabled = false;
}}

rangeslider2.onclick = function() {
	if (check2 == 0) {
		check2 = 1}; 
	rangeslider2.className = "clicked";
	if (check1 == 1 & check2 == 1) {
		confirm_button.disabled = false;
}}
	
var output1 = document.getElementById("belief_gering_gering");
output1.innerHTML = " "; 

rangeslider1.oninput = function() { 
	output1.innerHTML = this.value;
}

var output2 = document.getElementById("belief_gering_hoch");
output2.innerHTML = " "; 

rangeslider2.oninput = function() { 
	output2.innerHTML = this.value;
}