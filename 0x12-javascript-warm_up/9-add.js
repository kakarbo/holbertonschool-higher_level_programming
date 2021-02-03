#!/usr/bin/node
// Script that prints the addition of 2 integers

function add (a, b) {
  const result = Number.parseInt(a, 10) + Number.parseInt(b, 10);
  console.log(result);
}

add(process.argv[2], process.argv[3]);
