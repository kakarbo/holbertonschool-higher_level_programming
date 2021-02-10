#!/usr/bin/node
/*
Script that prints the title of a Star Wars movie where the episode
number matches a given integer
*/
const request = require('request');
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(requestURL, function (err, resp, body) {
  const json = JSON.parse(body);
  console.log(json.title);
  if (resp.statusCode === 404) {
    console.log(err);
  }
});
