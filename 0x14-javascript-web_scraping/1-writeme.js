#!/usr/bin/node
/* This script writes a string to a file.
    - the first argument it uses is the file path.
    - the second, is the string to write.
    - while the content of the file is writen in utf-8.
    - if an error occurred during the writing,it prints the error object.
*/

const fs = require('fs');
const file = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(file, stringToWrite, 'utf-8', errorFunc);

function errorFunc (err) {
  if (err) {
    console.log(err);
  }
}
