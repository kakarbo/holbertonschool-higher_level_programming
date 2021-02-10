#!/usr/bin/node
/*
Script that prints the number of movies where the character
"Wedge Antilles" is present
*/
const request = require('request');
request(process.argv[2], function (err, resp, body) {
  if (resp.statusCode === 404) {
    console.log(err);
  }
  const json = JSON.parse(body);
  let i = 0;
  let count = 0;
  for (let index in json) {
    /* eslint-disable no-unused-vars */
    index++;
    /* eslint-disable no-unused-vars */
    const people = json.results[i++].characters;
    for (const index of people) {
      if (index.endsWith('18/') === true) {
        count += 1;
      }
    }
  }
  console.log(count);
});
