#!/usr/bin/node
const Sqr = require('./5-square');
module.exports = class Square extends Sqr {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let s = '';
        for (let j = 0; j < this.width; j++) {
          s += c;
        }
        console.log(s);
      }
    }
  }
};
