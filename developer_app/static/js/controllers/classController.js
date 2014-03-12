function classController($scope, $http, $routeParams) {
      $http.get('api/v1/class/' + $routeParams.id + '?format=json').success(function(data){

          console.log(data);
          $scope.class = data;
          $scope.students = data.students;
          $scope.title = students.title;

      }

      }).error(function(data){
          console.log("You have an error in your code");
      });
}
