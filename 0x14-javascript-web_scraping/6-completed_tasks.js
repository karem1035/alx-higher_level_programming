#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (_err, __res, body) {
  const bodyArr = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < bodyArr.length; i++) {
    const userId = bodyArr[i].userId;
    if (bodyArr[i].completed && !dict[userId]) dict[userId] = 0;
    if (bodyArr[i].completed) dict[userId] += 1;
  }
  console.log(dict);
});
