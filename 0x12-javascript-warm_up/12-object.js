#!/usr/bin/node
// Script to replace the value 12 with 89
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
for (const prop in myObject) {
  myObject[prop] = 89;
}
console.log(myObject);
