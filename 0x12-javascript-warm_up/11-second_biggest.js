#!/usr/bin/node
// searches the second biggest integer in the list of arguments.

let biggest = 0;
let secBiggest = 0;

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] > biggest) {
      biggest = process.argv[i];
    }
  }
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] < biggest && process.argv[i] > secBiggest) {
      secBiggest = process.argv[i];
    }
  }
  console.log(secBiggest);
}
