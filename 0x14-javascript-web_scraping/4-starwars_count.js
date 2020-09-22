#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  let x = 0;
  const res = JSON.parse(body).results;
  for (const j of res) {
    for (const k of j.characters) {
      if (k === 'https://swapi-api.hbtn.io/api/people/18/') {
        x++;
      }
    }
  }
  console.log(x);
});
