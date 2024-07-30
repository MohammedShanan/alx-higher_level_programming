#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const starWarsApi = 'https://swapi-api.alx-tools.com/api/films/';
request.get(starWarsApi + movieId, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    function printInOrder (characters, index) {
      if (index >= characters.length) {
        return;
      }
      request.get(characters[index], function (err, response, body) {
        if (!err && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
          printInOrder(characters, index + 1);
        } else {
          console.log(err);
        }
      });
    }
    printInOrder(characters, 0);
  }
});
