#!/usr/bin/node
const args = process.argv;
if (!args[2] || !Number(args[2])) {
  console.log('Missing number of occurrences');
} else {
  const n = Number(args[2]);
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
