#!/usr/bin/node

/*  Thsi script gets the contents of a webpage and stores it in a file.
    - its first argument is the URL to request.
    - and its second argument is the file path to store the body response.
*/

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const nameFile = process.argv[3];

request(url, errorFunc);

function errorFunc (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(nameFile, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
}
