#!/usr/bin/node
import Rectangle from './4-rectangle';

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.height; col++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
