#!/usr/bin/node
// script that computes and prints a factorial
const n = process.argv[2];
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(parseInt(n)));
