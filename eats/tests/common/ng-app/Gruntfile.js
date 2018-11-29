module.exports = function (grunt) {
    //TODO refactor config paths
    var appFiles = {
            src: 'app/src',
            less: 'app/less',
            css: 'app/css',
            index: 'app/index.html',
            build: 'build'
        };

    require('load-grunt-config')(grunt, {
        data: {
            appFiles: appFiles
        }
    });
};
