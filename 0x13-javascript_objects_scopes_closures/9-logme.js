#!/usr/bin/node
let nbItem = 0;
exports.logMe = function (item) {
  console.log(nbItem + ': ' + item);
  nbItem++;
};
