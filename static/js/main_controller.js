var app = angular.module('app', ["chart.js"]);


function compare(a,b) {
  if ((a.erststimme + a.zweitstimme) > (b.erststimme + b.zweitstimme))
  return -1;
  if ((a.erststimme + a.zweitstimme) < (b.erststimme + b.zweitstimme))
  return 1;
  return 0;
}
app.controller("main_controller", function ($scope, $http){
  $scope.series = ['Erststimme', 'Zweitstimme'];
  $scope.colors = ['#FD1F5E','#1EF9A1','#7FFD1F','#68F000'];
 
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
              tableObject.erststimme = parseFloat(((tableObject.erststimme / all.erststimme)*100).toFixed(2))
              tableObject.zweitstimme = parseFloat(((tableObject.zweitstimme / all.zweitstimme)*100).toFixed(2))
              parties.push(tableObject)
            }
          }
        }
        parties = parties.sort(compare)
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
      })
    }

  });