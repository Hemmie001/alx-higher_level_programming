#!/usr/bin/node

// Convert a argument to an int
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arrNums = process.argv.slice(2).sort((a, b) => a - b);
  console.log(arrNums[arrNums.length - 2]);
}
