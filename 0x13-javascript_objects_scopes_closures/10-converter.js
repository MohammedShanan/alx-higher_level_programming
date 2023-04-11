#!/usr/bin/node

function converter (base) {
  function convert (n) {
    return n.toString(base);
  }
  return convert;
}
