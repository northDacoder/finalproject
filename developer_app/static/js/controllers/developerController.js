function developerController($scope, $http) {
    $http.get('api/v1/developer/?format=json').success(function(data){
        $scope.developers = data.objects;
        console.log($scope.developers);
    });

    $scope.addDeveloperProject = function() {
        console.log($scope.user);
        $http.post('api/v1/developers/', $scope.user).success(function(){
            alert('Add a developer project?');
        });
    }
}