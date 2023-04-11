#!/usr/bin/node

import { dict } from './101-data';

const newDic = {};
for (const key in dict) {
  if (newDic[dict[key]] === undefined) {
    newDic[dict[key]] = [];
  }
  newDic[dict[key]].push(key);
}

console.log(newDic);
