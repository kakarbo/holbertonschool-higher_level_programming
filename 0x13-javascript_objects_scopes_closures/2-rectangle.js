#!/usr/bin/node
// class Rectangle that defines a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.width = undefined;
      this.height = undefined;
    } else if (w === undefined || h === undefined) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
