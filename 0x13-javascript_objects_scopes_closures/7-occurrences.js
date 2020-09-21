#!/usr/bin/node
exports.nbOccurences = function (list, s) {
  let x = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === s) {
      x++;
    }
  }
  return x;
};
