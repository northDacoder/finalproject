app.controller('compController', function($scope) {
	$scope.companies = [
		name = '',
		city = '',
		github = '',
		email = '',
		user = ''
	];

	$scope.languages = [];

	$scope.companyProjects = [
		company = '',
		name = '',
		language = '',
		completed = '',
		user = ''
	];

	$scope.addCompany = function () {
		$scope.companies.push(
			name: $scope.new_company.name,
			city: $scope.new_company.city
		)
	}
});

app.config(function($scopeProvider){
	$routeProvider
		.when
			{
				controller: 'compController',
				template: 'companies.html'
			}
		.when
			{
				controller: 'compController',
				template: 'edit_company.html'
			}
		.when
			{
				controller: 'compController',
				template: 'new_company.html'
			}
		.when
			{
				controller: 'compController',
				template: 'view_company.html'
			}
		.otherwise({ redirectsTo: '/' });
});
/**
 * Created by northDacoder on 3/10/14.
 */


//app.controller('compController', function($scope, tastypieService) {
//    var companyService = new tastypieService({
//        apiUrl : '/api/v1/article/',
//        fk : {user : '/api/v1/user/'},
//        m2m : {comments : '/api/v1/comment/'},
//        editRelated : ['comments'],
//        keepFull : ['user']
//    });
//});


// INITIALIZE TASTYPIE
//<script>
//var someService = new tastypieService({
//    apiUrl : '<your API url here>',
//    fk : {
//        fk_field1 : '<foreign_key_field1_url>',
//        fk_field2 : '<foreign_key_field2_url>',
//        fk_field3 : '<foreign_key_field3_url>' // declare foreign key fields here
//    },
//    m2m : {
//        m2m_field1 : '<m2m_key_field1_url>',
//        m2m_field2 : '<m2m_key_field2_url>',
//        m2m_field3 : '<m2m_key_field3_url>' // declare m2m fields here
//    },
//    editRelated : [], // list fields that needs to be saved together (implements save_related in backend)
//    keepFull : [] // list fields that you don't want to save but still want to keep full (make sure you have full=True in your resource class)
//});
//</script>