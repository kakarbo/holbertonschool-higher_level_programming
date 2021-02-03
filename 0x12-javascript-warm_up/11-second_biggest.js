#!/usr/bin/node
// Script that searches the second biggest integer in the list of arguments
if (process.argv.length <= 2) {
  console.log('0');
} else if (process.argv.length === 3 && process.argv[2] === '1') {
  console.log('0');
} else {
  const myArray = [];
  for (let i = 2; i < process.argv.length; i++) {
    myArray.push(Number.parseInt(process.argv[i], 10));
  }
  const numberFirst = Math.max(...myArray);
  const pos = myArray.indexOf(numberFirst);
  for (let i = 0; i < myArray.length; i++) {
    if (numberFirst === myArray[i]) {
      myArray.splice(pos, 1);
    }
  }
  console.log(Math.max(...myArray));
}
