function developerProjectController($scope, $http) {
    $http.get('api/v1/developer/?format=json').success(function(data){
        $scope.projects = data.objects;
        console.log($scope.projects);
    });

    $scope.addDeveloperProject = function() {
        console.log($scope.user);
        $http.post('api/v1/developerproject/', $scope.user).success(function(){
            alert('Add a developer project?');
        });
    }
//
//    $scope.deleteDeveloperProject = function() {
//        console.log($scope.user);
//        $http.delete('api/v1/developerproject/', $scope.user).success(function(){
//            alert('You are trying to delete a developer project!');
//        });
//    }
}
