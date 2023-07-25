#!/usr/bin/node

/*  This script prints the title of a Star Wars movie such that episode number matches a given integer.
    - Where first argument is the movie ID.
    - the script uses Star Wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
*/

const request = require('request');
const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + id, function (err, resp, body) {
  if (resp.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.error(err);
  }
});
