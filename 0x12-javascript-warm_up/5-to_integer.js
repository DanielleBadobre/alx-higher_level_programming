#!/usr/bin/node
const argmt = process.argv;
const num = parseInt(argmt[2]);
if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
