var app = angular.module('app', ["chart.js"]);

app.controller("main_controller", function ($scope, $rootScope, $http){
  // the array contains modules that this module
  // depends on. In this case: none => empty array
  function compare(a,b) {
    if ((a.firstVotes + a.secondVotes) > (b.firstVotes + b.secondVotes))
      return -1;
    if ((a.firstVotes + a.secondVotes) < (b.firstVotes + b.secondVotes))
      return 1;
    return 0;
  }

  function addPercentage(list){
    var newList = []
    var validVotes = list[0]
    list.forEach(function(entry){
      if( entry.party !== "Gültige " ){
        var vp1 = (entry.firstVotes/validVotes.firstVotes * 100).toFixed(1)
        var vp2 = (entry.secondVotes/validVotes.secondVotes * 100).toFixed(1)

          var newPartyWithPercentage  = {party: entry.party, firstVotes:entry.firstVotes, secondVotes: entry.secondVotes, firstVotesPercentage: vp1, secondVotesPercentage: vp2};
          newList.push(newPartyWithPercentage)
        }})
        return newList
  }

  // constructor of the controller
  // variable $scope is the ViewModel
  
    $http.get('/states').success(function(response){
      var states = []
      console.log(response)
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
    
      $http.get('/constituency/'+ constituency).success(function(response){
        var response = JSON.parse(response)
        var parties = []
        var keys = [];
        var votes = []
        var oldString = '';
        console.log(response)
        for(var k in response){
          if(k !== 'Gebiet' && k !== 'Nr' && k !== 'serializable' && k !== 'gehört_zu' ){
          var tempString = k
          tempString = tempString.replace('Erststimmen', "")
          tempString = tempString.replace('Zweitstimmen', "")
          tempString = tempString.replace(/_/g, ' ')
          if(oldString != tempString){
           keys.push(tempString);
            oldString = tempString  
          }
          votes.push(response[k])
         }
        }
        var i = 0;
        var j = 0
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
        parties = addPercentage(parties)
        $scope.parties = parties
        $rootScope.$broadcast('partyData', parties)
      })
    }
  
    var parties = [];
    var primary = []
    var secondary = []
    // now get party information... 
    $rootScope.$on('partyData', function(event, data) {
      data.forEach(function(entry){
      if(entry.party !== "Wahlberechtigte" && entry.party !== "Wähler" && entry.party !=='Ungültige' && entry.party !== "Gültige" ){
       parties.push(entry.party)
       primary.push(entry.firstVotes)
       secondary.push(entry.secondVotes) 
      }})
     $scope.labels = parties;
     $scope.data = [
       primary, secondary
     ];
     $scope.colors = [["rgba(0, 0, 0, 1)",
     "rgba(255, 0, 0, 1)",
     "rgba(0, 255, 0, 1)",
     "rgba(0, 255, 255, 1)",
     "rgba(100, 255, 100, 1)"]]
    });
 

    var parties = [];
    var primary = []
    $rootScope.$on('partyData', function(event, data) {
     data.forEach(function(entry){
      if( entry.party !== "Wahlberechtigte" && entry.party !== "Wähler" && entry.party !=='Ungültige' && entry.party !== "Gültige" ){
      parties.push(entry.party)
      primary.push(entry.firstVotes)
     }})
    $scope.labels = parties;
    $scope.data = [
      primary
    ];
   });
 
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
   });
  });