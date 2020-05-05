#!/usr/bin/node
// a script that prints x times C is fun
const test = process.argv[2];
if (isNaN(test)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < test; i++) {
    console.log('C is fun');
  }
}
