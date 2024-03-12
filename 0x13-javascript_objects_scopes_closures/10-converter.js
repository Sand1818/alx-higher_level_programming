#!/usr/bin/node
exports.converter = function (base) {
    return function (convmun) {
      return convmun.toString(base);
    };
  };
  