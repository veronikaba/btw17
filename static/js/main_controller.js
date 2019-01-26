var app = angular.module('app', ["chart.js"]);

app.controller("main_controller", function ($scope, $rootScope, $http){
 
    $http.get('/states').success(function(response){
      var states = []
      for (var i = 0; i < response.length; i++){
        var state = {name: response[i][0], id: response[i][1]}
        states.push(state)
      }
      $scope.states = states
    }).error(function(response){
      console.log(response)
    });
    
    $scope.showConstituencies = function (state) {
      $http.get('/constituencies/'+ state.id).success(function(response){
        var constituencies = []
        for (var i = 0; i < response.length; i++){
          var constituency = {name: response[i][0], id: response[i][1]}
          constituencies.push(constituency)
        }
        $scope.constituencies = constituencies
      }).error(function(response){
        console.log(response)
      });
    }

    $scope.showDetails = function (constituency) {
      
      $http.get('/votes/'+ constituency.id).success(function(response){
        var response = JSON.parse(response)
        var parties = []
        var partyName = []
        var firstVotes = []
        var secondVotes = []
        var all = [];
      
        for(var i=3; i<response.length; i++){
          var tableObject = { party_name: response[i][1], erststimme:response[i][0].first_provisional_votes, zweitstimme: response[i][0].second_provisional_votes}
          if(i == 3){
            all = tableObject
          }
          else if(tableObject.erststimme || tableObject.zweitstimme){
            if(all){
              partyName.push(tableObject.party_name)
              firstVotes.push(tableObject.erststimme)
              secondVotes.push(tableObject.zweitstimme)
              tableObject.erststimme = ((tableObject.erststimme / all.erststimme)*100).toFixed(2)
              tableObject.zweitstimme = ((tableObject.zweitstimme / all.zweitstimme)*100).toFixed(2)
              parties.push(tableObject)
            }
          }
        }
        $scope.parties = parties
        $scope.labels = partyName;
        $scope.data = [
          firstVotes, secondVotes
        ];
        $scope.dataPieFirst = [
          firstVotes
        ];
        $scope.dataPieSecond = [
          secondVotes
        ];
        $scope.colors = ["rgba(0, 0, 0, 1)",
        "rgba(255, 0, 0, 1)",
        "rgba(0, 255, 0, 1)",
        "rgba(0, 255, 255, 1)",
        "rgba(100, 255, 100, 1)"]
      })
    }

  });