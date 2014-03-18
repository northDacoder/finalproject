function addDeveloperController($scope, $http) {
    console.log($scope.user);

    $http.post('api/v1/developer/', $scope.user).success(function(){
        alert('Add a Developer?');
    });
}
