#!/usr/bin/node

const a = process.argv;
const size = a.length;

function secondBiggest (a) {
  let first = parseInt(+a[0]);
  let second = parseInt(+a[0]);
  for (const i in a) {
    if (parseInt(+a[i]) >= first) {
      second = first;
      first = parseInt(+a[i]);
    } else if (parseInt(+a[i]) > second) {
      second = parseInt(+a[i]);
    }
  }
  return second;
}

if (size < 4) {
  console.log(0);
} else {
  console.log(secondBiggest(a.slice(2, size - 1)));
}
