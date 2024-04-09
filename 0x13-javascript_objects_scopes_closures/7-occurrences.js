#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let s; let k = 0;
    for (s = 0; s < list.length; s++) {
      if (list[s] === searchElement) {
        k++;
      }
    }
    return k;
  };
  