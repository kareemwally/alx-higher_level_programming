#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const filmURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(filmURL, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const characters = JSON.parse(body).characters;
  const charactersIds = [];
  for (let i = 0; i < characters.length; i++) {
    charactersIds.push(characters[i].slice(43, -1));
  }
  for (let j = 0; j < charactersIds.length; j++) {
    request(`https://swapi-api.alx-tools.com/api/people/${charactersIds[j]}`, function (err, response, body) {
      if (err) { console.log(err); }
      console.log(JSON.parse(body).name);
    });
  }
});
