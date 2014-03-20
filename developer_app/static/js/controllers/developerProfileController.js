function developerProfileController($scope, $http, $routeParams) {
     $http.get('api/v1/developers/' + $routeParams.id + '/?format=json').success(function(data){
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
//
//    $scope.deleteDeveloperProject = function() {
//        console.log($scope.user);
//        $http.delete('api/v1/developerproject/', $scope.user).success(function(){
//            alert('You are trying to delete a developer project!');
//        });
//    }

