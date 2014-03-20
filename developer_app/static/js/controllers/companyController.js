function companyController($scope, $http) {

    $http.get('api/v1/company/?format=json').success(function(data){
        $scope.companies = data.objects;
        console.log($scope.companies);
    });

    $scope.addCompanyProject = function() {
        console.log($scope.user);
        $http.post('api/v1/company/', $scope.user).success(function(){
            alert('Add a company project?');
        });
    }

}
