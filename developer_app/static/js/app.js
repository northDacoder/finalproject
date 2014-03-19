var app = angular.module('mvpApp', ['ui.bootstrap','ngRoute', 'ngResource']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', { templateUrl: '/static/views/index.html', controller: 'indexController' })
        .when('/developer', { templateUrl: '/static/views/developer.html', controller: 'developerController' })
        .when('/company', { templateUrl: '/static/views/company.html', controller: 'companyController' })
        .when('/contact', { templateUrl: '/static/views/contact.html' })
        .when('/add_developer', { templateUrl: '/static/views/add_developer.html', controller: 'addDeveloperController' })
        .when('/login/activate', { templateUrl: '/static/views/registration/delete_developer.html', controller: 'loginController' })
        .when('/login/activation_complete', { templateUrl: '/static/views/registration/activation_complete.html', controller: 'loginController' })
        .when('/login', { templateUrl: '/static/views/registration/login.html', controller: 'loginController' })
        .when('/login/logout', { templateUrl: '/static/views/registration/login.html', controller: 'loginController' })
        .when('/account/password_change_done', { templateUrl: '/static/views/registration/password_change_done.html', controller: 'loginController' })
        .when('/account/password_change_form', { templateUrl: '/static/views/registration/password_change_form.html', controller: 'loginController' })
        .when('/account/password_reset_complete', { templateUrl: '/static/views/registration/password_reset_complete.html', controller: 'loginController' })
        .when('/account/password_reset_confirm', { templateUrl: '/static/views/registration/password_reset_confirm.html', controller: 'loginController' })
        .when('/account/password_reset_done', { templateUrl: '/static/views/registration/password_reset_done.html', controller: 'loginController' })
        .when('/account/password_reset_email', { templateUrl: '/static/views/registration/password_reset_email.html', controller: 'loginController' })
        .when('/account/password_reset_form', { templateUrl: '/static/views/registration/password_reset_form.html', controller: 'loginController' })
        .when('/registration/closed', { templateUrl: '/static/views/registration/registration_closed.html', controller: 'loginController' })
        .when('/registration/complete', { templateUrl: '/static/views/registration/registration_closed.html', controller: 'loginController' })
        .when('/registration/form', { templateUrl: '/static/views/registration/registration_closed.html', controller: 'loginController' })

}]);