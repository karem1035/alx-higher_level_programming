#!/usr/bin/node
// returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((n, el) => (el === searchElement ? (n += 1) : n), 0);
};
