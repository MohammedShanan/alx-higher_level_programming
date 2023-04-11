#!/usr/bin/node

export function converter (base) {
  function convert (n) {
    return n.toString(base);
  }
  return convert;
}
