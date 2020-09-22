#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).films.length);
});
