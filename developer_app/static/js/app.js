var app = angular.module('mvpApp', ['ngRoute', 'ngResource']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', { templateUrl: '/static/views/index.html', controller: 'indexController' })
        .when('/class', { templateUrl: '/static/views/class.html', controller: 'classController' })
        .when('/student', { templateUrl: '/static/views/student.html', controller: 'classController' })
        .when('/addStudent', { templateUrl: '/static/views/add_student.html', controller: 'classController' })
        .when('/deleteStudent', { templateUrl: '/static/views/delete_student.html', controller: 'classController' })
        .when('/developer', { templateUrl: '/static/views/developer.html', controller: 'classController' })
        .when('/company', { templateUrl: '/static/views/company.html', controller: 'classController' })
        .when('/add_developer', { templateUrl: '/static/views/add_developer.html', controller: 'classController' })
        .when('/delete_developer', { templateUrl: '/static/views/delete_developer.html', controller: 'classController' });
}]);