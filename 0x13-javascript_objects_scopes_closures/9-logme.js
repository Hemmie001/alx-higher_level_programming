#!/usr/bin/node

// This js writes a function that prints the number of arguments already printed and the new argument value.
// using the Prototype: exports.logMe = function (item)
// Output format: <number arguments already printed>: <current argument value>

let pichu = 0;
exports.logMe = function (item) {
  console.log(pichu + ': ' + item);
  pichu++;
};
