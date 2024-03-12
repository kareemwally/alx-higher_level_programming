#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    } else {
      return Object.create(null);
    }
  }
}
module.exports = Rectangle;
