#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const starWarsApi = 'https://swapi-api.alx-tools.com/api/films/';
request.get(starWarsApi + movieId, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    console.log(jsonResponse.title);
  }
});
