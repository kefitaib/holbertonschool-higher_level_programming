#!/usr/bin/node
const arg = process.argv.slice(2);
console.log(process.argv[2])
const fs = require('fs');
fs.readFile(arg[0], function (err1, data1) {
  fs.readFile(arg[1], function (err2, data2) {
    if (err1 || err2) {
      throw new Error();
    }
    const data = data1 + data2;
    fs.writeFile(arg[2], data, function (err3) {
      if (err3) {
        throw new Error();
      }
    });
  });
});
