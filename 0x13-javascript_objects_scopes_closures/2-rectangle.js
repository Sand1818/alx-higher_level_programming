#!/usr/bin/node

const Rectangle = require("./0x13-javascript_objects_scopes_closures/0-rectangle");

module.exports = class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }
}

module.exports = Rectangle;