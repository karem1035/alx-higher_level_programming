#!/usr/bin/node
// Logging My number: <first argument converted in integer> if the first argument can be converted

if (!parseInt(process.argv[2])) console.log('Not a number');
else console.log(parseInt(process.argv[2]));
