#!/usr/bin/node

const a = process.argv;
const size = a.length;

function secondBiggest (a) {
  let first = a[0];
  let second = a[0];
  for (const i in a) {
    if (a[i] >= first) {
      if (a[i] > first) {
        second = first;
        first = a[i];
      }
    } else if (a[i] > second) {
      second = a[i];
    }
  }
  return second;
}

if (size < 4) {
  console.log(0);
} else {
  console.log(secondBiggest(a.slice(2, size - 1)));
}
