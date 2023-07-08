#!/usr/bin/node
// This js writes a class Rectangle that defines a rectangle:
// and uses the class notation for defining the class
// The constructor is made to take 2 arguments w and h
// it initializes the instance attribute width with the value of w,
// initializes the instance attribute height with the value of h.
// If w or h is equal to 0 or not a positive integer, create an empty object
// Create an instance method called print() that prints the rectangle using the character X

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // This is a  method, and it prints a rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
