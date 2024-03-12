#!/usr/bin/node
// mports an array and computes a new array.
let list = require('./100-main').list;
console.log(list);
list = list.map((el, i) => el * i);
console.log(list);
