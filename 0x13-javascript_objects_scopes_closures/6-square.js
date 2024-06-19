#!/usr/bin/node
const Square2 = require('./5-square.js');
module.exports = class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 1; i <= this.width; i++) {
      let row = '';
      for (let j = 1; j <= this.height; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
