#!/usr/bin/node
// Script that prints the first argument passed to it
let count = 0;
process.argv.forEach(() => {
  count += 1;
});
if (count <= 2) {
  console.log('No argument');
}
for (let i = 2; i < count; i++) {
  console.log(process.argv[i]);
}
