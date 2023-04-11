#!/usr/bin/node

export default class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let col = 0; col < this.height; col++) {
      console.log('X'.repeat(this.width));
    }
  }

    rotate () {
    let tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
