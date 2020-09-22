#!/usr/bin/node
const request = require('request');
const res = {};
let x = 1;
let c = 0;
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const b = JSON.parse(body);
  for (const i of b) {
    if (i.userId === x) {
      if (i.completed === true) {
        c++;
      }
    } else {
      res[String(x)] = c;
      c = 0;
      if (i.completed === true) {
        c++;
      }
      x = i.userId;
    }
  }
  res[String(x)] = c;
  console.log(res);
});
