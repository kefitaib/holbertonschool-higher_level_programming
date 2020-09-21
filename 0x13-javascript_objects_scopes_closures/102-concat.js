#!/usr/bin/node
var fs = require('fs');

fs.readFile(String(process.argv[2]), function (err1, data1) {
  fs.readFile(String(process.argv[3]), function (err2, data2) {
    if (err1 || err2) {
      throw new Error();
    }
    const data = data1 + data2;
    fs.writeFile(String(process.argv[4]), data, function (err3) {
      if (err3) {
        throw new Error();
      }
    });
  });
});
