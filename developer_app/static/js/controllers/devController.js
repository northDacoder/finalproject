app.controller('devController', function($scope) {
	$scope.developers = [
		name = '',
		city = '',
		github = '',
		languages = [],
		user = ''
	];

	$scope.languages = [

	];

	$scope.developerProjects = [
		developer = '',
		company = '',
		name = '',
		language = '',
		completed = '',
		user = ''
	];

	$scope.addDeveloper = function () {
		$scope.developers.push(
			name =
			city =
			github =
			languages =
			user =
		)
	}
});

app.config(function($scopeProvider){
	$routeProvider
		.when('/',
			{
				controller: 'devController',
				template: 'developers.html'
			})
		.when
			{
				controller: 'devController',
				template: 'edit_developer.html'
			}
		.when
			{
				controller: 'devController',
				template: 'new_developer.html'
			}
		.when
			{
				controller: 'devController',
				template: 'view_developer.html'
			}
		.otherwise({ redirectsTo: '/' });
});



//app.controller('devController', function($scope, tastypieService) {
//    var developerService = new tastypieService({
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