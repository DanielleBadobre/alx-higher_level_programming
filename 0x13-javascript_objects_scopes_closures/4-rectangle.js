#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      let row = '';
      for (let j = 1; j <= this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const newW = this.height;
    const newH = this.width;
    this.width = newW;
    this.height = newH;
  }

  double () {
    const doubleW = 2 * this.width;
    const doubleH = 2 * this.height;
    this.width = doubleW;
    this.height = doubleH;
  }
}
module.exports = Rectangle;
