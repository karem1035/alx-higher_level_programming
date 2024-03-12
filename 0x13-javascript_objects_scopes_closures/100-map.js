#!/usr/bin/node
// mports an array and computes a new array.
const list = require('./100-data').list;
console.log(list);
console.log(list.map((el, i) => el * i));
