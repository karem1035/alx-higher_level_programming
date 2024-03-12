#!/usr/bin/node
const dict = require('./101-data').dict;
console.log(dict);

const nDict = {};

for (const key in dict) {
  nDict[dict[key]] ? nDict[dict[key]].push(key) : (nDict[dict[key]] = [key]);
}

console.log(nDict);
