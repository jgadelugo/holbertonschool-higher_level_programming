#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

try {
  const source = fs.readFileSync(argv[2], 'utf8');
  console.log(source);
} catch (err) {
  console.log(err);
}
