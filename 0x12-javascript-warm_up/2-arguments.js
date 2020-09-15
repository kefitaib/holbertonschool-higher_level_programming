#!/usr/bin/node
if (process.argv[2] !== undefined) {
  if (process.argv[3] === undefined) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
} else {
  console.log('No argument');
}
