#!/usr/bin/node
const argmt = process.argv;
if (!(argmt[2])) {
  console.log('No argument');
} else {
  console.log(argmt[2]);
}
