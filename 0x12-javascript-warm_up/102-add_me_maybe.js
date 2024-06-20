#!/usr/bin/node
function theFunction (number) {
  console.log(number);
}
function addMeMaybe (number, theFunction) {
  number += 1;
  return theFunction(number);
}
module.exports = { addMeMaybe };
