#!/usr/bin/node
// Script that prints a square
const numberArgument = Number.parseInt(process.argv[2], 10);
let myStrig = 'X'
if (Number.isNaN(numberArgument)) {
  console.log('Missing size');
} else {
  for (let i = 1; i < numberArgument; i++){
    myStrig += 'X';
  }
  for (let i = 1; i <= numberArgument; i++) {
    for (let j = i; j <= i; j++) {
		console.log(myStrig);
    }
  }
}
