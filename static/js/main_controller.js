(function () {
  // the array contains modules that this module
  // depends on. In this case: none => empty array
  var app = angular.module('app', []);

  // constructor of the controller
  // variable $scope is the ViewModel
  app.controller("main_controller", function ($scope) {
    $scope.all_names = ["A", "B", "c"];
  });
})();
