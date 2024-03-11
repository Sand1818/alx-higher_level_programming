#!/usr/bin/node
let a = process.argv[2];

if (isNaN(a)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    let msg = '';
    for (let j = 0; j < a; j++) {
      msg = msg + 'X';
    }
    console.log(msg);
  }
}