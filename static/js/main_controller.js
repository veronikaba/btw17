var app = angular.module('app', ["chart.js"]);
  // the array contains modules that this module
  // depends on. In this case: none => empty array


  // constructor of the controller
  // variable $scope is the ViewModel
  app.controller("main_controller", function ($scope, $rootScope, $http) {
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
    
    $scope.showConstituencies = function (state) {
      $http.get('/constituencies/'+ state).success(function(response){
        var response = JSON.parse(response)
        var constituencies = []
        for (var i = 0; i < response.length; i++){
          constituencies[i] = response[i].serializable.Gebiet;
        }
        $scope.constituencies = constituencies
      }).error(function(response){
        console.log(response)
      });
    }
    $scope.showDetails = function (constituency) {
    
      $http.get('/constituency/'+ constituency).success(function(response){
        var response = JSON.parse(response)
        var parties = []
        var keys = [];
        var votes = []
        var oldString = '';
        for(var k in response){
          if(k !== 'Gebiet' && k !== 'Nr' && k !== 'serializable' && k !== 'gehört_zu'){
          var tempString = k.replace(/_/g, ' ')
          tempString = tempString.replace('Erststimmen', "")
          tempString = tempString.replace('Zweitstimmen', "")
          if(oldString != tempString){
           keys.push(tempString);
            oldString = tempString  
          }
          votes.push(response[k])
         }
        }
        var i=0;
        var j =0
        while (i < keys.length){
        // every vote votes on pos j %2 =0 is first vote else second
        var party = {party:keys[i], firstVotes:votes[j], secondVotes: votes[j+1] };
         i = i+1 
         j = j+2
         parties.push(party)
        }
        $scope.parties = parties
        $rootScope.$broadcast('partyData', parties)
      })
    }
  });

  app.controller('bar_controller', function($scope){
    var parties = [];
    var primary = []
    var secondary = []
    // now get party information... 
    for( var i in $scope.parties){
        parties.push(parties[i].party)
        primary.push(parties[i].firstVotes)
        secondary.push(parties[i].secondVotes)
    }
    $scope.labels = parties
    $scope.data = [
      [65, 59, 80, 81, 56, 55, 40],
      [28, 48, 40, 19, 86, 27, 90]
    ];
  });

  app.controller('firstVotes_pie_ctrl', function($scope, $rootScope){
    var parties = [];
    var primary = []
    $rootScope.$on('partyData', function(event, data) {
     var d = data
     data.forEach(function(entry){
      parties.push(entry.party)
      var j= "" + JSON.stringify(entry.firstVotes) 
      if(entry.firstVotes){
        j = parseInt(entry.firstVotes)
      }else{
        j =0
      }
      primary.push(j)
     })
     console.log('parties' + parties)
     console.log('primary' +primary)
    $scope.labels = parties;
    $scope.data = [
      [primary]
    ];
   });
  });

  app.controller('secondVotes_pie_ctrl', function($scope){
    $scope.labels = ['2006', '2007', '2008', '2009', '2010', '2011', '2012'];
    $scope.data = [
      [28, 48, 40, 19, 86, 27, 90]
    ];
  });

