#!/usr/bin/node
import Rectangle from './4-rectangle';

export default class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
