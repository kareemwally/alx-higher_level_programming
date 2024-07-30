#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, function (err, respose, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
