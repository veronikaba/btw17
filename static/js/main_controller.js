var app = angular.module('app', []);
(function () {
  // the array contains modules that this module
  // depends on. In this case: none => empty array

  // constructor of the controller
  // variable $scope is the ViewModel
  app.controller("main_controller", function ($scope) {
    $scope.states = [
      "Baden-Wüttemberg",
      "Bayern",
      "Berlin",
      "Brandenburg",
      "Bremen",
      "Hamburg",
      "Hessen",
      "Mecklenburg-Vorpommern",
      "Niedersachsen",
      "Nordreihn-Westfalen",
      "Reihnland-Pfalz",
      "Saarland",
      "Sachsen",
      "Sachsen-Anhalt",
      "Schleswig-Holstein",
      "Thüringen",
    ];

    $scope.showConstituencies = function () {
      $scope.constituencies = [
        "Berlin-Charlottenburg-Wilmersdorf",
        "Berlin-Friedrichshein-Kreuzberg-Prenzlauerberg Ost",
        "Berlin-Lichtenberg",
        "Berlin-Marzah-Hellerdorf",
      ];
      /*constituencies.push($scope.test);*/
    }
  });

})(app);
