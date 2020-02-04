#!/usr/bin/node

const a = process.argv;
const size = a.length;

function secondBiggest (a) {
  const unique = [...new Set(a)];
  if (unique.length < 2) {
    return unique[0];
  }
  unique.sort();
  unique.reverse();
  return unique[1];
}

if (size < 4) {
  console.log(0);
} else {
  console.log(secondBiggest(a.slice(2, size)));
}
