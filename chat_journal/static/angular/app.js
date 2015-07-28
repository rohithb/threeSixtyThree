(function(){
    var app = angular.module('feedApp', ['angularMoment']);
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });

    app.constant('angularMomentConfig', {

        format: 'YYYY-MM-DDThh:mm:ss'
    });

    app.controller('feedCtrl', function($scope, $http) {
        $http.get("/list-posts/")
        .success(function(response) {$scope.feeds = response;});
    });
})();
