#!/usr/bin/node
const arg = parseInt(Process.argv[2], 10);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${arg}`);
}
