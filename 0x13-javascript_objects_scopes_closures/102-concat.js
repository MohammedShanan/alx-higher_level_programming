#!/usr/bin/node

let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
import { readFileSync, writeFileSync } from 'fs';
let textA = readFileSync(fileA, 'utf8');
let textB = readFileSync(fileB, 'utf8');
writeFileSync(fileC, textA + textB);
