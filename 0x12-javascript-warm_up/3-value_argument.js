#!/usr/bin/node
// script that prints the first argument passed to it
const test = process.argv[2];
if (test === undefined) {
  console.log('No argument');
} else {
  console.log(test);
}
