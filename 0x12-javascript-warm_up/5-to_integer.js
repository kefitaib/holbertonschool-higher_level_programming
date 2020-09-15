#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No number');
} else {
  const n = parseInt(process.argv[2], 10);
  if (isNaN(n)) {
    console.log('No number');
  } else {
    console.log('My number: ' + n);
  }
}
