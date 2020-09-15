#!/usr/bin/node
if (process.argv.length === 3 || process.argv.length === 2) {
  console.log(0);
} else {
  let big;
  let big2;
  if (parseInt(process.argv[2]) < parseInt(process.argv[3])) {
    big = parseInt(process.argv[3]);
    big2 = parseInt(process.argv[2]);
  } else {
    big = parseInt(process.argv[2]);
    big2 = parseInt(process.argv[3]);
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > big) {
      big2 = big;
      big = parseInt(process.argv[i]);
    }
    if (big2 < parseInt(process.argv[i]) && parseInt(process.argv[i]) < big) {
      big2 = parseInt(process.argv[i]);
    }
  }
  console.log(big2);
}
