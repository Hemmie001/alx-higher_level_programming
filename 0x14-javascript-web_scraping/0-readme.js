#!/usr/bin/node
/* This script reads and prints the content of a file.
    - the first argument is the file path.
    - the content of the file is read in utf-8.
    - if an error occurred during the reading, it prints the error object.
*/

const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8', errorFunc);

function errorFunc (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}
