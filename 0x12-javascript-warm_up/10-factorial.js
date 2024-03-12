#!/usr/bin/node
const x = parseInt(process.argv[2]);
function fac (a) {
  if (isNaN(a) || a === 0) {
    return (1);
  }
  return a * fac(a - 1);
}
console.log(fac(x));
