#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
    }
 
    print () {
        let s, k;
        for (s = 0; s < this.height; s++) {
            for (k = 0; k < this.width; k++) {
                process.stdout.write('X');
            }
            process.stdout.write('\n');
        }
    }
}

module.exports = Rectangle;