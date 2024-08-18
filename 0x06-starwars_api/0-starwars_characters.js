#!/usr/bin/env node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Syntax: ./0-starwars_characters.js <movieID>');
  process.exit(1);
}

const movieID = process.argv[2];

const FILMS_URL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

const options = {
  url: FILMS_URL,
  method: 'GET'
};

request(options, async (err, res, body) => {
  if (err) {
    process.exit(1);
  }
  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
});
