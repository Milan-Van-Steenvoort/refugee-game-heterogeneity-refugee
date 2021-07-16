/* Contains actions to perform for pages containing primary slider items, not specific to the continuous or discrete
 * version */

/* Register all confirmation button event handlers */

$("#item7_confirm").click(function() {

		$("#item7").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item8_confirm").click(function() {

		$("#item8").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item9_confirm").click(function() {

		$("#item9").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item10_confirm").click(function() {

		$("#item10").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item11_confirm").click(function() {

		$("#item11").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item12_confirm").click(function() {

		$("#item12").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item13_confirm").click(function() {

		$("#item13").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item14_confirm").click(function() {

		$("#item14").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );

$("#item15_confirm").click(function() {

		$("#item15").slider("disable");
		$(this).prop('disabled', true);
		$(this).val("True");

	}
    );


/* On submit, check if all choices are confirmed. If not: display error and do not submit */
$("#continue_button").click(function() {
        if (check_all_confirmed(7, 15)) {
            $("#hidden_submit_button").click();
        }
        else {
            $("#confirmation_error").show();
            window.scrollTo(0, 0);
        }
    }
    );

/* Execute on script load */

// Update all start and end values
for (i = 7; i <= 15; i++) {
    update_by_id('item' + i + '_self_start', allocation_bounds['item' + i]['self_left']);
    update_by_id('item' + i + '_self_end', allocation_bounds['item' + i]['self_right']);
    update_by_id('item' + i + '_other_start', allocation_bounds['item' + i]['other_left']);
    update_by_id('item' + i + '_other_end', allocation_bounds['item' + i]['other_right']);
}