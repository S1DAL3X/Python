$('document').ready(function() {
	$('body').on('click', '.about-us-popup-link', function(event) {
		$('#about_us_popup').toggle();
		if ($('#about_us_popup').is(':visible')) {
			$('#about_us_popup_link').addClass('about-us-popup-link-active');
		} else {
			$('#about_us_popup_link').removeClass('about-us-popup-link-active');
		}
	});
	$('body').on('click', '.policy-popup-link', function(event) {
		$('#policy_popup').toggle();
	});
	$('body').on('click', '.pp-close-button', function(event) {
		$('#policy_popup').hide();
	});
});