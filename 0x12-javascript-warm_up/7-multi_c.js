#!/usr/bin/node
// Script that prints x times 'C is fun'
const numberArgumet = Number.parseInt(process.argv[2], 10);
if (Number.isNaN(numberArgumet)) {
  console.log('Missing number of occurrences');
} else {
	for (let i = 0; i < numberArgumet; i++) {
		console.log('C is fun');
	}
}
