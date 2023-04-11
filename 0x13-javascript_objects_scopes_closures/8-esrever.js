#!/usr/bin/node

export function esrever (list) {
  let start = 0;
  let end = list.length - 1;
  while (start < end) {
    let tmp = list[start];
    list[start] = list[end];
    list[end] = tmp;
    start++;
    end--;
  }
  return list;
}
