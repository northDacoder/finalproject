var app = angular.module('mvpApp', ['ngRoute', 'mobile-angular-ui', 'mobile-angular-ui.touch', 'mobile-angular-ui.scrollable', 'ngResource']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', { templateUrl: '/static/views/index.html', controller: 'indexController' })
        .when('/developers', { templateUrl: '/static/views/developers.html', controller: 'developerController' })
        .when('/companies', { templateUrl: '/static/views/companies.html', controller: 'companyController' })
        .when('/contact', { templateUrl: '/static/views/contact.html' })
        .when('/about', { templateUrl: '/static/views/about.html' })
        .when('/user/:id', { templateUrl: '/static/views/user.html', controller: 'userController' })
        .when('/login/activate', { templateUrl: '/static/views/registration/delete_developer.html', controller: 'loginController' })
        .when('/login/activation_complete', { templateUrl: '/static/views/registration/activation_complete.html', controller: 'loginController' })
        .when('/login', { templateUrl: '/static/views/registration/login.html', controller: 'loginController' })
        .when('/login/logout', { templateUrl: '/static/views/registration/login.html', controller: 'loginController' })
        .when('/accounts/password/reset', { templateUrl: '/static/views/registration/password_reset_form.html', controller: 'loginController' })
        .when('/accounts/password/change/done', { templateUrl: '/static/views/registration/password_change_done.html', controller: 'loginController' })
        .when('/accounts/password/change/form', { templateUrl: '/static/views/registration/password_change_form.html', controller: 'loginController' })
        .when('/accounts/password/reset/complete', { templateUrl: '/static/views/registration/password_reset_complete.html', controller: 'loginController' })
        .when('/accounts/password/reset/confirm', { templateUrl: '/static/views/registration/password_reset_confirm.html', controller: 'loginController' })
        .when('/accounts/password/reset/done', { templateUrl: '/static/views/registration/password_reset_done.html', controller: 'loginController' })
        .when('/accounts/password/reset/email', { templateUrl: '/static/views/registration/password_reset_email.html', controller: 'loginController' })
//      .when('/accounts/password_reset_email', { templateUrl: '/static/views/registration/password_reset_email.html', controller: 'loginController' })
        .when('/registration/closed', { templateUrl: '/static/views/registration/registration_closed.html', controller: 'loginController' })
        .when('/registration/complete', { templateUrl: '/static/views/registration/registration_closed.html', controller: 'loginController' })
        .when('/registration/form', { templateUrl: '/static/views/registration/registration_closed.html', controller: 'loginController' })

}]);