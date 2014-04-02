function developerController($scope, $http) {

    $http.get('api/v1/developer/?format=json').success(function(data){
        $scope.developers = data.objects;
        console.log($scope.developers);
    });

//    $http.get('api/v1/developerproject/?format=json').success(function(data){
//        $scope.projects = data.objects;
//        console.log($scope.projects);
//    });
}