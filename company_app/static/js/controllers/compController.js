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
