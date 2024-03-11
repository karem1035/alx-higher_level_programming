#!/usr/bin/node
// Logging the fitst command line argument
if (process.argv.length < 3) console.log('No argument');
else console.log(process.argv[2]);
