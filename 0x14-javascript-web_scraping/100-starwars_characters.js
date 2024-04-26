#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, function (_err, __res, body) {
  const chars = JSON.parse(body).characters;

  for (let i = 0; i < chars.length; i++) {
    request(chars[i], function (_err, __res, body) {
      console.log(JSON.parse(body).name);
    });
  }
});
