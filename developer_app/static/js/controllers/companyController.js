function companyController($scope, $http) {
    $http.get('api/v1/company/?format=json').success(function(data){
        console.log(data);
        $scope.companies = data.objects;
    });
//    }).error(function(data){
//        console.log("You have an error in your code");
//    });

}
