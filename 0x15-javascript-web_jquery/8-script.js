/*
Script that fetches and lists the title for all movies by using this
URL: https://swapi-api.hbnt.api/api/films/?format=json
*/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const index of data.results) {
    $('#list_movies').append('<li>' + index.title + '</li>');
  }
});
