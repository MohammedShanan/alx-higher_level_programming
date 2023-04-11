#!/usr/bin/node

import { readFileSync, writeFileSync } from 'fs';
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const textA = readFileSync(fileA, 'utf8');
const textB = readFileSync(fileB, 'utf8');
writeFileSync(fileC, textA + textB);
