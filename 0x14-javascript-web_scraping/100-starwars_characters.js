#!/usr/bin/node

/*  this script prints all characters of a Star Wars movie.
    - its first argument is the Movie ID.
    - and it displays one character name by line.
*/

const request = require('request');
const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + id, function (err, resp, body) {
  if (resp.statusCode === 200) {
    for (const url of JSON.parse(body).characters) {
      request(url, function (error, response, body2) {
        if (resp.statusCode === 200) {
          console.log(JSON.parse(body2).name);
        } else {
          console.error(error);
        }
      });
    }
  } else {
    console.error(err);
  }
});
