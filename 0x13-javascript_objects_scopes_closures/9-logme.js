#!/usr/bin/node

let num = 0;
export function logMe (item) {
  console.log(num + ': ' + item);
  num++;
}
