#!/usr/bin/node

// This js is a function that converts a number from base 10 to another base passed as argument:
// with the use of the Prototype: exports.converter = function (base)
// ...does not import any file
// & does not declare any new variable (var, let, etc..)
exports.converter = function (base) {
  return function (num) {
    return parseInt(num, 10).toString(base);
  };
};
