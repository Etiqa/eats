(function (app) {
    'use strict';

    function ApplicationCtrl ($scope) {
        this.textField = null;
        this.placeHolder = null;
        this.textFieldFull = "Hello World";
        this.checkField = false;
        this.checkFieldTrue = true;
        this.radioField = 'yes';
        this.passwdField = null;
        this.selectField = {id: 1, value: 'option 1'};

        this.selectOptions = [
            {id: 1, value: 'option 1'},
            {id: 2, value: 'option 2'},
            {id: 3, value: 'option 3'},
            {id: 4, value: 'option 4'}
        ];

        $scope.testBind = 'test binding';
    }
    function PageCtrl () {
        this.textField = null;
        this.checkField = false;
        this.radioField = 'yes';
        this.passwdField = null;
        this.selectField = {id: 1, value: 'option 1'};

        this.selectOptions = [
            {id: 1, value: 'option 1'},
            {id: 2, value: 'option 2'},
            {id: 3, value: 'option 3'},
            {id: 4, value: 'option 4'}
        ]
    }

    app.controller('AppController', ['$scope', ApplicationCtrl]);
    app.controller('PageController', [PageCtrl]);


}(angular.module('ngTestForm', [])));
