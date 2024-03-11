#!/usr/bin/node
let x = process.argv;
console.log(x[2] === undefined ? 'No argument' : x[2])
