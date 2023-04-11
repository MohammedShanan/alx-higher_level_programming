#!/usr/bin/node
import { list } from './100-data';

const newList = list.map((x, index) => x * index);

console.log(list);
console.log(newList);
