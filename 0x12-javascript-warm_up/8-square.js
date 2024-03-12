#!/usr/bin/node
const x = process.argv;
const y = parseInt(x[2]);
if (isNaN(y)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let i = 0; i < y; i++) {
    row += 'X';
  }
  for (let j = 0; j < y; j++) {
    console.log(row);
  }
}
