#!/usr/bin/node
const request = require('request');
let x = 0;
request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const res = JSON.parse(body).results;
  for (const j of res) {
    if (j) {
      for (const k of j.characters) {
        if (k && k === 'https://swapi-api.hbtn.io/api/people/18/') {
          x++;
        }
      }
    }
  }
  console.log(x);
});
