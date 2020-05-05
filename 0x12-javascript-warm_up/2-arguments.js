#!/usr/bin/node
// script that prints a message depending
// of the number of arguments passed
const test = process.argv.length;
if (test === 2) {
  console.log('No argument');
} else if (test === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
