#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, data1) => {
  if (err) console.log('Error reading fileA');
  fs.readFile(fileB, 'utf-8', (err, data2) => {
    if (err) console.log('Error reading fileB');
    const data = data1 + data2;
    fs.writeFile(fileC, data, (err) => {
      if (err) console.log('Error writing to fileC');
    });
  });
});
