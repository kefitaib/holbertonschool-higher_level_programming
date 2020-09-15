#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No number');
} else {
  console.log('My number: ' + parseInt(process.argv[2], 10));
}
