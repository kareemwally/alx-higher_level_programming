#!/usr/bin/node
const x = process.argv;
const y = parseInt(x[2]);
if (isNaN(y)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + y);
}
