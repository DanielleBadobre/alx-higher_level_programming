#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const [id, occurences] of Object.entries(dict)) {
  if (!newDict[occurences]) {
    newDict[occurences] = [];
  }
  newDict[occurences].push(id);
}
console.log(newDict);
