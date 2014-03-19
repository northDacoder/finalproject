function companyProjectController($scope, $http) {

    $scope.addCompanyDeveloperProject = function() {
        console.log($scope.user);
        $http.post('api/v1/companyproject/', $scope.user).success(function(){
            alert('Add a developer project?');
        });
    }

    $scope.deleteCompanyDeveloperProject = function() {
        console.log($scope.user);
        $http.delete('api/v1/companyproject/', $scope.user).success(function(){
            alert('You are trying to delete a developer project!');
        });
    }
}
