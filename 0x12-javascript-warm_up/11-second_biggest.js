#!/usr/bin/node
const numsArray = process.argv.slice(2);
function secondMax (array) {
  let max = -Infinity;
  let secMax = -Infinity;
  if (array.length < 2) {
    return (0);
  }
  for (const num of array) {
    if (num > max) {
      secMax = max;
      max = num;
    } else if (num < max && num > secMax) {
      secMax = num;
    }
  }
  return (secMax);
}
console.log(secondMax(numsArray));
