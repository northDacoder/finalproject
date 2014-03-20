function developerController($scope, $http) {
    $http.get('api/v1/developer/?format=json').success(function(data){
        console.log(data);

        $scope.developers = data.objects;
    });

    $scope.addDeveloperProject = function() {
        console.log($scope.user);
        $http.post('api/v1/developers/', $scope.user).success(function(){
            alert('Add a developer project?');
        });
    }
//
//    $scope.deleteDeveloperProject = function() {
//        console.log($scope.user);
//        $http.delete('api/v1/developer/', $scope.user).success(function(){
//            alert('You are trying to delete a developer project!');
//        });
//    }
}
