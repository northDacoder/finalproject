function companyController($scope, $http) {

    $http.get('api/v1/company/?format=json').success(function(data){
        $scope.companies = data.objects;
        console.log($scope.companies);
    });
//
//    this.style = {
//        "background-color":"red",
//        "height":"200px",
//        //"background-image":"url(http://placekitten.com/200/300)"
//    };
//
//    this.style1 = 'blue';
//    this.style2 = 'http://placekitten.com/200/300';
//    this.style3 =  "url(http://placekitten.com/200/300)";

}
