#!/usr/bin/node
exports.esrever = function (list) {
    let aList = [];
    for (let s = list.length - 1; s > -1; s--) {
      aList.push(list[s]);
    }
    return aList;
  };