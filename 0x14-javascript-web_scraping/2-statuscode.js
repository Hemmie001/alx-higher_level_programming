#!/usr/bin/node

/*  This script displays the status code of a GET request.
    - its first argument is the URL to request (GET).
    - and its output should be like: 'code: <status code>'.
*/

const request = require('request');
const url = process.argv[2];
request.get(url).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});
