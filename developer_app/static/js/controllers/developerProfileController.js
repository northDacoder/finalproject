function developerProfileController($scope, $http, $routeParams) {
     $http.get('api/v1/developer/' + $routeParams.id + '/?format=json').success(function(data){
        console.log(data);
        $scope.userprofile = data.objects;
    });

    $scope.addDeveloperProject = function() {
        console.log($scope.user);
        $http.post('api/v1/developers/', $scope.user).success(function(){
            alert('You reached your profile!');
        });
    }
}

