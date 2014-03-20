function userController($scope, $http, $routeParams) {
     $http.get('api/v1/developer/' + $routeParams.id + '/?format=json').success(function(data){
        console.log(data);
        $scope.userprofile = data.objects;
    });

}

