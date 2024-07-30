#!/usr/bin/node
const request = require('request');
const starWarsApi = process.argv[2];
request.get(starWarsApi, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movie of movies) {
      for (const Character of movie.characters) {
        if (Character.endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
