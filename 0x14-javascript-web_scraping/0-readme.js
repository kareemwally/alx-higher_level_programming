#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const encoding = 'utf-8';
fs.readFile(filename, encoding, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
