#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3]; // Use process.argv[3] for the file name
request(url, function (__error, __response, body) {
  fs.writeFile(file, body, function (__err) {});
});
