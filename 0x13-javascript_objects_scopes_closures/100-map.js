#!/usr/bin/node
// mports an array and computes a new array.
const list = require('./100-main').list;
console.log(list);
const nList = list.map((el, i) => el * i);
console.log(nList);
