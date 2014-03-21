function companyController($scope, $http) {

    $http.get('api/v1/company/?format=json').success(function(data){
        $scope.companies = data.objects;
        console.log($scope.companies);
    });

    $http.get('api/v1/companyproject/?format=json').success(function(data){
        $scope.companyprojects = data.objects;
        console.log($scope.companyprojects);
    });

//    $scope.addCompanyProject = function() {
//        console.log($scope.user);
//        $http.post('api/v1/company/', $scope.user).success(function(){
//            alert('Add a company project?');
//        });
//    }

}
