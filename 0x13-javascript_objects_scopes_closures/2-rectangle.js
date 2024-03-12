#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.height = h > 0 && w > 0 ? h : undefined;
    this.width = w > 0 && h > 0 ? w : undefined;
  }
}
module.exports = Rectangle;
