#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    fs.writeFile(filename, jsonResponse, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
