#!/usr/bin/node
let x = process.argv;
let y = parseInt(x[2]);
if (isNaN(y))
{
console.log('Not a number');
}
else
{
console.log('My number: ' + y);
}
