#!/usr/bin/node
// script that searches the second biggest
// integer in the list of arguments.
if (process.argv.length < 4) {
  console.log('0');
} else {
  const args = process.argv.slice(2).map(Number);
  const test = args.sort(function (a, b) { return b - a; })[1];
  console.log(test);
}
