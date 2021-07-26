/* Contains variables and actions specific to the continuous version of the slider measure */

var continuous_final_number = 100;

/* Create each slider and attach the necessary event handlers */
var confirm_button = document.getElementById("button_id");

var item7_slider = $('#item7').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item7', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item7_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item7', proportional_position_on_slider);
}).data('slider');

var item8_slider = $('#item8').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item8', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item8_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item8', proportional_position_on_slider);
}).data('slider');

var item9_slider = $('#item9').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item9', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item9_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item9', proportional_position_on_slider);
}).data('slider');

var item10_slider = $('#item10').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item10', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item10_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item10', proportional_position_on_slider);
}).data('slider');

var item11_slider = $('#item11').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item11', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item11_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item11', proportional_position_on_slider);
}).data('slider');

var item12_slider = $('#item12').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item12', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item12_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item12', proportional_position_on_slider);
}).data('slider');

var item13_slider = $('#item13').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item13', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item13_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item13', proportional_position_on_slider);
}).data('slider');

var item14_slider = $('#item14').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item14', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item14_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item14', proportional_position_on_slider);
}).data('slider');

var item15_slider = $('#item15').slider({
    formatter: function(value) {
        var proportional_position_on_slider = value / continuous_final_number;
        return tooltip_text('item15', proportional_position_on_slider);
    }
}).on('change',  function () {
    var value = item15_slider.getValue();
    var proportional_position_on_slider = value / continuous_final_number;
    update_displayed_values('item15', proportional_position_on_slider);
    confirm_button.disabled = false;
    confirm_button.innerHTML = "Next";
}).data('slider');



/* Update all displayed values for the first time */

update_displayed_values('item7', item2_slider.getValue() / continuous_final_number);
update_displayed_values('item8', item3_slider.getValue() / continuous_final_number);
update_displayed_values('item9', item4_slider.getValue() / continuous_final_number);
update_displayed_values('item10', item5_slider.getValue() / continuous_final_number);
update_displayed_values('item11', item6_slider.getValue() / continuous_final_number);
update_displayed_values('item12', item6_slider.getValue() / continuous_final_number);
update_displayed_values('item13', item6_slider.getValue() / continuous_final_number);
update_displayed_values('item14', item6_slider.getValue() / continuous_final_number);
update_displayed_values('item15', item6_slider.getValue() / continuous_final_number);

/* See SVO citizen as to  why this is here
                            <div class="col-sm-2"><button type="button" class="btn btn-primary btn-large" id="item{{ item_number }}_confirm" value="False">Confirm</button></div>

    <button type="button" class="btn btn-primary btn-large" id="continue_button" >Continue</button>
    <button id="hidden_submit_button" type="submit" hidden="True"></button>
    */