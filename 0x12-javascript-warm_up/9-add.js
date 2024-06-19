#!/usr/bin/node
// script adds to numbers
const args = process.argv;
function add (a, b) {
  a = Number(args[2]);
  b = Number(args[3]);
  console.log(a + b);
}
add();
