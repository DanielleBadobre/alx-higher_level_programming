#!/usr/bin/node
// computes and prints a factorial

function factorial (a) {
  if (a === 1 || isNaN(a) || a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
