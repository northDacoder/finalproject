var app = angular.module('mvpApp', ['ngRoute', 'ngResource']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/',
            {
                templateUrl: '/static/views/index.html',
                controller: 'indexController'
            })
        .when('/class',
            {
                templateUrl: '/static/views/class.html',
                controller: 'classController'
            });
)]);