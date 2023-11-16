#!/usr/bin/node
// Checking the arugments

const args = process.argv; 
if (args.length === 2) {
  console.log("Argument found");
} else if (args.length > 2) {
  console.log("Arguments found");
} else {
  console.log("No argument");
}
