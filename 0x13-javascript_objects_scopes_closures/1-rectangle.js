#!/usr/bin/node
// This js writes a class Rectangle that defines a rectangle:
// and uses the class notation for defining the class
// The constructor is made to take 2 arguments w and h
// it initializes the instance attribute width with the value of w,
// initializes the instance attribute height with the value of h.
// If w or h is equal to 0 or not a positive integer, create an empty object

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
