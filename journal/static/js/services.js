// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('journalApp.services', ['ngResource'])
    .factory('Post', function($resource){
        return $resource('/api/posts/:id');
    })
    .factory('User', function(){
        return $resource('/api/users/:id');
    })
