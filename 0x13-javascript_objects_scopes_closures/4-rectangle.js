#!/usr/bin/node
// class Rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      /* eslint-disable no-unused-vars */
      const person = {};
      /* eslint-disable no-unused-vars */
    } else if (w === undefined || h === undefined) {
      /* eslint-disable no-unused-vars */
      const person = {};
      /* eslint-disable no-unused-vars */
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // method
  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  print () {
    let myString = 'X';
    for (let i = 1; i < this.width; i++) {
      myString += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = i; j <= i; j++) {
        console.log(myString);
      }
    }
  }
};
