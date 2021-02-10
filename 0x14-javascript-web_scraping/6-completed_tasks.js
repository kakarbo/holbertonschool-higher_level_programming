#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const obj = {};
  for (const json of JSON.parse(body)) {
    if (json.completed) {
      if (obj[json.userId]) {
        obj[json.userId] += 1;
      } else {
        obj[json.userId] = 1;
      }
    }
  }
  console.log(obj);
});
