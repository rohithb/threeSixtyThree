
var app = angular.module('journalApp', [
    'angularMoment',
    'ngRoute',
    'ngResource',
    'journalApp.services',
    'journalApp.controllers',
    ])
    .config(function($interpolateProvider, $httpProvider, $resourceProvider, $routeProvider, $locationProvider) {
        // Force angular to use square brackets for template tag
        $interpolateProvider.startSymbol('[[').endSymbol(']]');

        // CSRF Support
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';

        // It makes dealing with Django slashes at the end of everything easier.
        $resourceProvider.defaults.stripTrailingSlashes = false;


        // Routing

        $routeProvider
            .when('/posts', {
                templateUrl: 'static/partials/post-list.html',
                controller: 'PostController',
            })
            .when('/profile', {
                templateUrl: 'static/partials/profile.html',
                controller: 'UserController',
            })
            .otherwise({
                redirectTo: '/posts'
            });
        
    });

app.constant('angularMomentConfig', {

    format: 'YYYY-MM-DDThh:mm:ss'
});