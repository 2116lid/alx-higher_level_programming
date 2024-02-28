//etches and lists the title for all movies by using a URL

const url = 'https://swapi-api.hbtn.io/api';

$.get(`${url}/films/?format=json`, function(data, status) {
	data.results.forEach(film => {
		$('ul#list_movies').append(`<li>${film.title}</li>`);
	});
});
