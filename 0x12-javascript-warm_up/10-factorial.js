#!/usr/bin/node
function factoriel (numm) {
    if (numm >= 1) { return (numm * factoriel(numm - 1)); } else { return (1); }
  }

  if (process.argv.length === 2) {
    console.log('1');
  } else if (process.argv.length === 3) {
    console.log(factoriel(parseInt(process.argv[2])));
  }