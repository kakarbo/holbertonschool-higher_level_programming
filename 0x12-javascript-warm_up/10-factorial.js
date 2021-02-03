#!/usr/bin/node
// Script that computes and prints a factorial
function factorial (n) {
  let total = 0;
  if (n === 0 || process.argv.length <= 2) {
    return 1
  } else {
    total = n * factorial(n - 1);
  }
  return total;
}
factor = factorial(Number.parseInt(process.argv[2], 10));
console.log(factor);
