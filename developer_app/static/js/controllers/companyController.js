function companyController($scope, $http) {

    $http.get('api/v1/company/?format=json').success(function(data){
        $scope.companies = data.objects;
        console.log($scope.companies);
    });

}
