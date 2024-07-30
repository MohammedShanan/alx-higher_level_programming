#!/usr/bin/node
const request = require("request");
const starWarsApi = process.argv[2];
request.get(starWarsApi, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (let movie of movies) {
      console.log(movie.Characters);
    //   for (let Character of movie["Characters"]) {
    //     console.log(Character);
    //     if (Character.endsWith("/18/")) {
    //       count++;
    //     }
      }
    }
    console.log(count);
  }
});
