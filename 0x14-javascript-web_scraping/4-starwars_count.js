#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, respose, body) {
  if (err) {
    console.log(err);
  }
  let res = 0;
  const characterlist = JSON.parse(body).results;
  for (let i = 0; i < 7; i++) {
    const temp = characterlist[i].characters;
    for (let j = 0; j < temp.length; j++) {
      if (temp[j].includes('18')) { res++; }
    }
  }
  console.log(res);
});
