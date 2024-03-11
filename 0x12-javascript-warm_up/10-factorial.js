#!/usr/bin/node
// computes and prints a factorial
function fact(n) {
  if (n) return n * fact(n - 1);
  else return 1;
}
const n = process.argv[2];
console.log(fact(n));
