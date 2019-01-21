var app = angular.module('app', ["chart.js"]);
  // the array contains modules that this module
  // depends on. In this case: none => empty array
  function compare(a,b) {
    if ((a.firstVotes + a.secondVotes) > (b.firstVotes + b.secondVotes))
      return -1;
    if ((a.firstVotes + a.secondVotes) < (b.firstVotes + b.secondVotes))
      return 1;
    return 0;
  }

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
          if(k !== 'Gebiet' && k !== 'Nr' && k !== 'serializable' && k !== 'gehört_zu' ){
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
        var v1 =0;
        var v2 =0;
        if(votes[j]){
          v1 = parseInt(votes[j]);
        }
        if(votes[j+1]){
          v2 = parseInt(votes[j+1]);
        }
        var party = {party:keys[i], firstVotes:v1, secondVotes: v2 };
         i = i+1 
         j = j+2
         parties.push(party)
        }
        parties = parties.sort(compare)
        $scope.parties = parties
        $rootScope.$broadcast('partyData', parties)
      })
    }
  });

  app.controller('bar_controller', function($scope, $rootScope){
    var parties = [];
    var primary = []
    var secondary = []
    // now get party information... 
    $rootScope.$on('partyData', function(event, data) {
      data.forEach(function(entry){
      if(entry.party !== "Wahlberechtigte " && entry.party !== "Wähler " && entry.party !=='Ungültige ' && entry.party !== "Gültige " ){
       parties.push(entry.party)
       primary.push(entry.firstVotes)
       secondary.push(entry.secondVotes) 
      }})
     $scope.labels = parties;
     $scope.data = [
       primary, secondary
     ];
    });
  });

  app.controller('firstVotes_pie_ctrl', function($scope, $rootScope){
    var parties = [];
    var primary = []
    $rootScope.$on('partyData', function(event, data) {
     data.forEach(function(entry){
      if( entry.party !== "Wahlberechtigte " && entry.party !== "Wähler " && entry.party !=='Ungültige ' && entry.party !== "Gültige " ){
      parties.push(entry.party)
      primary.push(entry.firstVotes)
     }})
    $scope.labels = parties;
    $scope.data = [
      primary
    ];
    $scope.colors = ["rgba(224, 108, 112, 1)",
            "rgba(224, 108, 112, 1)",
            "rgba(224, 108, 112, 1)"]
   });
  });

  app.controller('secondVotes_pie_ctrl', function($scope, $rootScope){
    var parties = [];
    var secondary = []
    $rootScope.$on('partyData', function(event, data) {
     data.forEach(function(entry){
      if(entry.party !== "Wahlberechtigte " && entry.party !== "Wähler " && entry.party !=='Ungültige ' && entry.party !== "Gültige " ){
        parties.push(entry.party)
        secondary.push(entry.secondVotes)
     }})
    $scope.labels = parties;
    $scope.data = [
      secondary
    ];
    $scope.colors = ['#72C02C', '#3498DB', '#717984', '#F1C40F'];
   });
  });

