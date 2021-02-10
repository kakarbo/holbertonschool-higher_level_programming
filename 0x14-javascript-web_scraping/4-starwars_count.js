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
  let count = 0;
  for (const index of json.results) {
    for (const character of index.characters) {
      if (character.endsWith('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
