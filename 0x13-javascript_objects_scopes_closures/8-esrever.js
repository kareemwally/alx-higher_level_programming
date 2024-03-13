#!/usr/bin/node
exports.esrever = function (list) {
  const res = [];
  for (let i = list.length - 1; i > -1; i--) {
    res.push(list[i]);
  }
  return res;
};
