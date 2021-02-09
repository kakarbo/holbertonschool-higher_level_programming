#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  const newList = [];
  let lengt = list.length;
  for (let index = 0; index < list.length; index++) {
    lengt--;
    newList[index] = list[lengt];
  }
  return newList;
};
