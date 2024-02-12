#!/usr/bin/node
const arg = parseInt(process.argv[2], 10);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}
