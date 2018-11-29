'use strict';

module.exports = function (grunt, options) {
    return {
        options: {
            basePath: 'app'
        },
        mytarget: {
            src: options.appFiles.index,
            dest: options.appFiles.index
        }
    };
};
