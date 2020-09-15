#!/usr/bin/node
function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return factorial(a - 1) * a;
  }
}

if (process.argv[2] === undefined) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
