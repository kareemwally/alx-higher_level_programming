#!/usr/bin/node
const x = process.argv;
const y = parseInt(x[2]);
if (isNaN(y)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < y; i++) {
    console.log('C is fun');
  }
}
