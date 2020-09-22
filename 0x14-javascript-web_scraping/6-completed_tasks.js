#!/usr/bin/node
const request = require('request');
const res = {};
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const b = JSON.parse(body);
  for (const i of b) {
    if (i.completed === true) {
      if (res[i.userId]) {
        res[i.userId] += 1;
      } else {
        res[i.userId] = 1;
      }
    }
  }
  console.log(res);
});
