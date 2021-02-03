#!/usr/bin/node
/*
Script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/
const number = Number.parseInt(process.argv[2], 10);
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
