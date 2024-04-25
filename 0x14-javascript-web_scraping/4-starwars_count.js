#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const person = '18';
let counter = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const resultsArray = JSON.parse(body).results;
  for (let i = 0; i < resultsArray.length; i++) {
    const characters = resultsArray[i].characters;
    for (let j = 0; j < characters.length; j++) { if (characters[j].split('/')[5] === person) counter++; }
  }
  console.log(counter);
});
