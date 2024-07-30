#!/usr/bin/node
const fs = require("fs");
const filename = process.argv[1];
fs.readFile(filename, "utf8", (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
