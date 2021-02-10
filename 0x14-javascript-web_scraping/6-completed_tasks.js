#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body);
  let count = 0;
  let num = 1;
  const obj = {};
  for (const index in json) {
    for (let i = 0; i <= 10; i++) {
      if (json[index].userId === i) {
        if (i !== num) {
          count = 0;
          num++;
        }
        if (json[index].completed === true) {
          count += 1;
        }
        obj[i] = count;
      }
    }
  }
  console.log(obj);
});
