#!/usr/bin/node
// updating the Rectangle class
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h) {
      this.width = w;
      this.height = h;
    }
  }
};
