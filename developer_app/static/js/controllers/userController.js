function userController($scope, $http, $routeParams) {
    $http.get('api/v1/developer/' + $routeParams.id).success(function(data){
        console.log(data);
        $scope.profile = data;
    });

}

