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
				template: 'base.html'
			}
		.when
			{
				controller: 'devController',
				template: 'home.html'
			}
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
