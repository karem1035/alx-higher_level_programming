#!/usr/bin/node
const dict = require('./101-data').dict;

const nDict = {};

for (const key in dict) {
  nDict[dict[key]] ? nDict[dict[key]].push(key) : (nDict[dict[key]] = [key]);
}

console.log(nDict);
