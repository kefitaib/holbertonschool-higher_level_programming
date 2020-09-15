#!/usr/bin/node
if (process.argv.length === 3 || process.argv.length === 2) {
  console.log(0);
} else {
  let big;
  let big2;
  if (process.argv[2] < process.argv[3]) {
    big = process.argv[3];
    big2 = process.argv[2];
  } else {
    big = process.argv[2];
    big2 = process.argv[3];
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (process.argv[i] > big) {
      big2 = big;
      big = process.argv[i];
    }
    if (big2 < process.argv[i] && process.argv[i] < big) {
      big2 = process.argv[i];
    }
  }
  console.log(big2);
}
