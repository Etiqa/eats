'use strict';

module.exports = function (grunt, options) {
    return {
        task: {
            src: [options.appFiles.index],
            options: {}
        }
    };
};
