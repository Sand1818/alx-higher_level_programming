#!/usr/bin/node
function add (s, j) {
    console.log(parseInt(s) + parseInt(j));
  }
  add(process.argv[2], process.argv[3]);