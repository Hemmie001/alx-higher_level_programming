#!/usr/bin/node

/* This script prints the number of movies where the character “Wedge Antilles” is present.
    - the first argument is the API URL of the Star wars API.
    - and wedge Antilles is character ID 18 (the script use this ID for filtering the result).
*/

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (err, resp, body) {
  // console.log(resp.statusCode)
  if (resp.statusCode === 200) {
    for (const result of JSON.parse(body).results) {
      for (const character of result.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
  } else {
    console.error(err);
  }
  console.log(count);
});
