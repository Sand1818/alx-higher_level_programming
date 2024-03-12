#!/usr/bin/node
let logmcount = -1;
exports.logMe = function (item) {
  logmcount++;
  console.log(logmcount + ': ' + item);
};