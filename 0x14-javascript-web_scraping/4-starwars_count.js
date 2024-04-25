#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const person = 'https://swapi-api.alx-tools.com/api/people/18/';
let counter = 0;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode === 200) {
    const resultsArray = JSON.parse(body).results;
    let i;

    for (i = 0; i < resultsArray.length; i++) {
      if (resultsArray[i].characters.includes(person)) counter++;
    }
    console.log(counter);
  } else console.log(response.statusCode);
});
