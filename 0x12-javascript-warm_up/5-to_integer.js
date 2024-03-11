#!/usr/bin/node
// Logging My number: <first argument converted in integer> if the first argument can be converted

if (isNaN(process.argv[2])) console.log('Not a number');
else console.log(`My number: ${parseInt(process.argv[2])}`);
