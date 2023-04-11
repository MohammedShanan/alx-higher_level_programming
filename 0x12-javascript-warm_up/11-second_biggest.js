#!/usr/bin/node
const numsArray = process.argv.slice(2);
function secondMax (array) {
  let max = -Infinity;
  let secMax = -Infinity;
  if (array.length < 2) {
    return (0);
  }
  for (let i = 0; i < array.length; i++) {
    if (array[i] > max) {
      secMax = max;
      max = array[i];
    } else if (array[i] < max && array[i] > secMax) {
      secMax = array[i];
    }
  }
  return (secMax);
}
console.log(secondMax(numsArray));
