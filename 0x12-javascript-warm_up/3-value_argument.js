#!/usr/bin/node
// Script that prints the first argument passed to it
let count = 0;
process.argv.forEach(() => {
  count += 1;
});
if (count <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
