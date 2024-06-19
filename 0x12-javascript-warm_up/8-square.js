#!/usr/bin/node
// script prints a square
const args = process.argv;
if (!args[2] || !Number(args[2])) {
  console.log('Missing size');
} else {
  let result = '';
  for (let i = 0; i < Number(args[2]); i++) {
    for (let j = 0; j < Number(args[2]); j++) {
      result += 'X';
    }
    console.log(result);
    result = '';
  }
}
