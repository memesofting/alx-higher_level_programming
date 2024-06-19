#!/usr/bin/node
// script computes factorial of a number

const args = process.argv;
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n < 0) {
    return;
  }
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const n = Number(args[2]);
const result = factorial(n);
console.log(result);
