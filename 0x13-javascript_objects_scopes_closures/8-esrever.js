#!/usr/bin/node

#This function writes a function that returns the reversed version of a list:
#it uses the prototype: exports.esrever = function (list)
# This script is without the use of built-in method reverse

exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev[list.length - i - 1] = list[i];
  }
  return rev;
};
