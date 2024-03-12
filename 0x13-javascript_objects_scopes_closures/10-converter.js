#!/usr/bin/node
// Convert N to base
exports.converter = function (base) {
  return (num) => num.toString(base);
};
