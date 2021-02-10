#!/usr/bin/node
/*
Script that prints the number of movies where the character
"Wedge Antilles" is present
*/
const request = require('request');
const peopleURL = 'https://swapi-api.hbtn.io/api/people/18/';
request(process.argv[2], function (err, resp, body) {
  if (resp.statusCode === 404) {
    console.log(err);
  }
  const json = JSON.parse(body);
  let i = 0;
  let count = 0;
  for (const index in json) {
    const people = json["results"][i++]["characters"];
    for (const index of people) {
      if (index === peopleURL) {
        count += 1;
      }
    }
  }
  console.log(count);
});
