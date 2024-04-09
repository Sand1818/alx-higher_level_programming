#!/usr/bin/node
class Rectangle {
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

    rotate () {
        const w = this.width;
        this.width = this.height;
        this.height = w;
    }

    double () {
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;
