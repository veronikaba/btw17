(function(){
    // the array contains modules that this module
    // depends on. In this case: none => empty array
    var app = angular.module('app', []);

    // constructor of the controller
    // variable $scope is the ViewModel
    app.controller('main-controller', function($scope){
        // in this simple example: nothing to do
        // in more realistic examples:
        // initialize the controller
    });
}());