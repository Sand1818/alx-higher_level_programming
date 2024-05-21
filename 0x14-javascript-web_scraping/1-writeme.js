#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
const str = process.argv[3];
fs.writeFile(filename, str, (error) => {
  if (error) throw error;
});
