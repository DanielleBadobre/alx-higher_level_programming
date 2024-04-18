#!/usr/bin/node
// prints square

const argmt = process.argv;
const size = parseInt(argmt[2]);
let x = '';

if (!isNaN(size)) {
  for (let i = 1; i <= size; i++) {
    x += 'X';
  }
  for (let j = 1; j <= size; j++) {
    console.log(x);
  }
} else {
  console.log('Missing size');
}
