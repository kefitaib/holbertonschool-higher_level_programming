#!/usr/bin/node
let s = '';
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    s = '';
    for (let j = 0; j < process.argv[2]; j++) {
      s += 'X';
    }
    console.log(s);
  }
}
