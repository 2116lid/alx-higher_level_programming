//fethes from a url and displays hello

const url = 'https://fourtonfish.com';

$.get(`${url}/hellosalut/?lang=fr`, function(data, status) {
	$('div#hello').html(data.hello);
});
