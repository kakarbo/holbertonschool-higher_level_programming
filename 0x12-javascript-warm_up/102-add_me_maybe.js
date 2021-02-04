#!/usr/bin/node
// Function that increments and calls a function
exports.addMeMaybe = function (n, theFunction) {
  theFunction(n += 1);
};
