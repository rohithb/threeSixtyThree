 var journalControllers = angular.module('journalApp.controllers', []);

 journalControllers.controller('PostController', function PostCtrl($scope, Post, AuthUser){
     $scope.posts ={};

     Post.query(function(response){
        $scope.posts = response;
     });

     $scope.summitPost = function(newPost){
        var post = new Post({body: newPost});
        post.$save(function(response){
            $scope.posts.push(response);
        });
     }
 })

 journalControllers.controller('UserController', function UserCtrl($scope, User, AuthUser){
    id = AuthUser.id;
    User.get({id:id}, function(response){
        $scope.user = response;
    });
 });