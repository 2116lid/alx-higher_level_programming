//fetches the character name from a url

const url = 'https://swapi-api.hbtn.io/api';

$.get(`${url}/people/5/?format=json`, function(data, status) {
	$('div#character').html(data.name);
});
