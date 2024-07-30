#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonResponse = JSON.parse(body);
    const tasks = {};
    for (const task of jsonResponse) {
      if (task.completed === true) {
        tasks[task.userId] = (tasks[task.userId] || 0) + 1;
      }
    }
    console.log(tasks);
  }
});
