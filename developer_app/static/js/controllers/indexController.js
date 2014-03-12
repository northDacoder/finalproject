function indexController($scope, $http, RocketSpace) {

    console.log(RocketSpace.angular_instructor);

    $scope.classes = {
        "1st Cohort": "Group 1",
        "2nd Cohort": "Group 2"
    };

    $http.get('api/v1/student/?format=json').success(function(data){
        console.log(data.objects);
        $scope.students = data.objects;
        RocketSpace.student_list = $scope.students;
    });

    $http.get('api/v1/class/?format=json').success(function(data){
        console.log(data.objects);
        $scope.classes = data.objects;
    });
}