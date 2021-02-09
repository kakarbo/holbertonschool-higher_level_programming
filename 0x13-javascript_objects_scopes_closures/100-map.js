#!/usr/bin/node
// script that imports an array and computes a new array
const list = require('./100-data').list;
console.log(list);
for (let index = 0; index < list.length; index++) {
  list[index] *= index;
}
console.log(list);
