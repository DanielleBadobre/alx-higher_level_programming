#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  let ind = 0;
  for (let i = (list.length - 1); i >= 0; i--) {
    revList[ind] = list[i];
    ind++;
  }
  return revList;
};
