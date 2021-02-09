#!/usr/bin/node
// function that returns the number of ocurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const index of list) {
    if (searchElement === index) {
      count++;
    }
  }
  return count;
};
