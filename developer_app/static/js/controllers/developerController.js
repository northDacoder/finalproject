function developerController($scope, $http) {
    $http.get('api/v1/developer/?format=json').success(function(data){
        console.log(data);

        $scope.developers = data.objects;
//    }).error(function(data){
//        console.log("You have an error in your code");
//    });
//
//
//    $scope.user = {'klass': "api/v1/company/1/", 'projects':[]};
//
//    $scope.addDeveloper = function() {
//        console.log($scope.user);
//        $http.post('api/v1/developer/', $scope.user).success(function(){
//            alert('Add a Developer?');
//        });
//    }
//
//    $scope.deleteDeveloper = function() {
//        console.log($scope.user);
//        $http.delete('api/v1/developer/', $scope.user).success(function(){
//            alert('You are trying to delete a Developer!');
//        });
//    }
};
