#!/usr/bin/node
const dict = require('./101-data').dict;
const d = dict;
const res = {};
for (const v of Object.values(dict)) {
  const l = [];
  for (const [k1, v1] of Object.entries(d)) {
    if (v === v1) {
      l.push(String(k1));
      delete d.k1;
    }
  }
  res[String(v)] = l;
}

console.log(res);
