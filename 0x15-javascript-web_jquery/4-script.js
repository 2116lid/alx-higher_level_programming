//toggles the class header

$('div#toggle_header').on('click', function() {
	if ($('header').hasClass('red')) {
		$('header').removeClass('red');
		if (!$('header').hasClass('green')) {
			$('header').addClass('green');
		}
	} else if ($('header').hasClass('green')) {
		$('header').removeClass('green');
		if (!$('header').hasClass('red')) {
			$('header').addClass('red');
		}
	} else {
		$('header').addClass('red');
	}
});
