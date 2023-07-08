#!/usr/bin/node

// This js writes a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
// It uses the class notation for defining its class and extends
// it create an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, it uses the character X

const Square01 = require('./5-square');

module.exports = class Square extends Square01 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let m = 0; m < this.height; m++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
