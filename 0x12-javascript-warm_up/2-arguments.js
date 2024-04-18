#!/usr/bin/node
const argmt = process.argv;
if (!(argmt[2])) {
  console.log('No argument');
}
if ((argmt[2]) && !(argmt[3])) {
  console.log('Argument found');
}
if ((argmt[3])) {
  console.log('Arguments found');
}
