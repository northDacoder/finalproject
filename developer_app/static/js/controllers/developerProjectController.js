function developerProjectController($scope, $http) {

    $scope.addDeveloperProject = function() {
        console.log($scope.user);
        $http.post('api/v1/developer/', $scope.user).success(function(){
            alert('Add a developer project?');
        });
    }

    $scope.deleteDeveloperProject = function() {
        console.log($scope.user);
        $http.delete('api/v1/developer/', $scope.user).success(function(){
            alert('You are trying to delete a developer project!');
        });
    }
}
