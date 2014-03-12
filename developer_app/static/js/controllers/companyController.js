function companyController($scope, $http) {
    $http.get('api/v1/company/?format=json').success(function(data){
        console.log(data);

    }).error(function(data){
        console.log("You have an error in your code");
    });


    $scope.user = {'klass': "api/v1/company/1/", 'projects':[]};

    $scope.addStudent = function() {
        console.log($scope.user);
        $http:post('api/v1/company/', $scope.user).success(function(){
            alert('Add a Company?');
        });
    }

    $scope.deleteStudent = function() {
        console.log($scope.user);
        $http:delete('api/v1/student/', $scope.user).success(function(){
            alert('You are trying to delete a student!');
        });
    }
};
