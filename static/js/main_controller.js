var app = angular.module('app', ["chart.js"]);
  // the array contains modules that this module
  // depends on. In this case: none => empty array

  // constructor of the controller
  // variable $scope is the ViewModel
  app.controller("main_controller", function ($scope, $http) {
    $http.get('/states').success(function(response){
      var response = JSON.parse(response)
      var states = []
      for (var i = 0; i < response.length; i++){
        states[i] = response[i][0];
      }
      $scope.states = states
    }).error(function(response){
      console.log(response)
    });
    
    $scope.showConstituencies = function () {
     // console.log($scope.states[0])
      var param = $scope.states[0]
      $http.get('/constituencies',{params:{param}}).success(function(response){
        $scope.constituencies = response
      }).error(function(response){
        console.log(response)
      });
    }
  });

  app.controller('bar_controller', function($scope){
    $scope.labels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012'];
  
    $scope.data = [
      [65, 59, 80, 81, 56, 55, 40],
      [28, 48, 40, 19, 86, 27, 90]
    ];
  });

  app.controller('firstVotes_pie_ctrl', function($scope){
    $scope.labels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012'];
    $scope.data = [
      [28, 48, 40, 19, 86, 27, 90]
    ];
  });

  app.controller('secondVotes_pie_ctrl', function($scope){
    $scope.labels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012'];
    $scope.data = [
      [28, 48, 40, 19, 86, 27, 90]
    ];
  });

