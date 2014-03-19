function profileController($scope, $http, $routeParams) {

    $http.get('api/v1/myProfile/' + $routeParams.id + '?format=json').success(function(data){
        console.log(data);
        $scope.profile = data.objects;
    });

}
