#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films';

request(url, function (_err, __res, body) {
  const charArray = JSON.parse(body).results[movieID].characters;
  for (let i = 0; i < charArray.length; i++) {
    request(charArray[i], function (_err, __res, body) {
      console.log(JSON.parse(body).name);
    });
  }
});
