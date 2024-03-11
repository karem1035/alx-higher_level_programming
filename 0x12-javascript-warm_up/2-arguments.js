#!/usr/bin/node
// Checking if there is a command line argument/s or not
if (process.argv.length < 3) console.log('No argument');
else if (process.argv.length === 3) console.log('Argument found');
else console.log('Arguments found');
