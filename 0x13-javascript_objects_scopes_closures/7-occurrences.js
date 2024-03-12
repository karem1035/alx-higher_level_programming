#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (const el of list) {
    if (el === searchElement) n += 1;
  }
  return n;
};
