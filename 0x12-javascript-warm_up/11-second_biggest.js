#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.
if (process.argv.length <= 3) console.log(0);
else {
  const arr = process.argv.sort().reverse();
  console.log(arr[1]);
}
