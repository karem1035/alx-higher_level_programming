#!/usr/bin/node
// Converts the argument to integer if possible

const intValue = parseInt(process.argv[2]);

if (!isNaN(intValue)) {
  console.log("My number: " + intValue);
} else {
  console.log("Not a number");
}
