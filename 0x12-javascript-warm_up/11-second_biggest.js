#!/usr/bin/node
const numsArray = process.argv.slice(2);
function secondMax (array) {
  let max = -Infinity;
  let secMax = -Infinity;
  if (array.length < 2) {
    return (0);
  }
  for (let i = 0; i < array.length; i++) {
    const num = parseInt(array[i], 10);
    if (num > max) {
      secMax = max;
      max = num;
    } else if (num < max && num > secMax) {
      secMax = num;
    }
  }
  if (secMax === -Infinity) {
    return (max);
  }
  return (secMax);
}
console.log(secondMax(numsArray));
