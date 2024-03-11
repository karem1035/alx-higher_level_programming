#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.
const arr = process.argv.slice(2).map((el) => parseInt(el));
if (arr.length <= 1) console.log(0);
else console.log(arr.sort((a, b) => b - a)[1]);
