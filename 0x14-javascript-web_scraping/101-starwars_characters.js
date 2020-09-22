#!/usr/bin/node
const request = require('request');
const l = {};
let x = 0;
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const b = JSON.parse(body);
  for (const i of b.characters) {
    request(i, function (err1, response1, body1) {
      if (err1) {
        console.log(err1);
      }
      l[i] = JSON.parse(body1).name;
      x++;
      if (x === b.characters.length) {
        Object.values(l).forEach(val => { console.log(val); });
      }
    });
  }
});
