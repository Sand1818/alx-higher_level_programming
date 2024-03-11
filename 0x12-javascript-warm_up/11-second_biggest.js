#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) { console.log('0'); } else {
    let i;
    let first = Number.MIN_VALUE;
    let second = Number.MIN_VALUE;
    for (i = 0; i < process.argv.length; i++) {
      if (parseInt(process.argv[i]) > first) {
        second = first;
        first = parseInt(process.argv[i]);
      } else if (parseInt(process.argv[i]) > second && parseInt(process.argv[i]) < first) { second = parseInt(process.argv[i]); }
    }
    console.log(second);
  }