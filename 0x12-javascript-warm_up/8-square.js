#!/usr/bin/node
// a script that prints a square
const test = process.argv[2];
if (isNaN(test)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < test; i++) {
    console.log('X'.repeat(test));
  }
}
