function companyController($scope, $http) {
    $http.get('api/v1/company/?format=json').success(function(data){
        console.log(data);
        $scope.companies = data.objects;
    });

    $http.get('api/v1/company/?format=json').success(function(data){
        console.log(data);
        $scope.projects = data.objects;
    });

}
