#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    let cWidth = '';
    for (let i = 0; i < this.width; i++) {
      cWidth += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(cWidth);
    }
  }
};
