#!/usr/bin/node
const argmt = process.argv;
const occ = parseInt(argmt[2]);
if (!isNaN(occ)) {
  for (let i = 1; i <= occ; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
