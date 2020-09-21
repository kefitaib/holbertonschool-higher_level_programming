#!/usr/bin/node
exports.esrever = function (list) {
  const l = [];
  for (let i = 0, j = list.length - 1; j >= 0; j--, i++) {
    l[i] = list[j];
  }
  return l;
};
