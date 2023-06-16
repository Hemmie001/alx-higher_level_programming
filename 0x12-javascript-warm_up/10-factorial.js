#!/usr/bin/node
function Factorial (n) {
  if (!n) {
    return (1);
  }
  if (n !== 0) {
    return (n * Factorial(n - 1));
  }
}
const { argv } = require('process');
const n = parseInt(argv[2]);
console.log(Factorial(n));
