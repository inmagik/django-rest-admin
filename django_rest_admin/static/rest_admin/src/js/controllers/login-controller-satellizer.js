(function(){
"use strict";

angular.module('app')
.controller('LoginCtrl', LoginCtrl);

function LoginCtrl($scope, $auth, $rootScope){

    $scope.credentials = {
        username : 'admin',
        password : 'admin123'
    };

    $scope.loginError = null;
    
    $scope.login = function(){
        $auth.login($scope.credentials)
        .then(function(response) {
            // Redirect user here after a successful log in.
            $rootScope.$broadcast("app:loginSuccess", response);
            console.log("login success", response);
        })
        .catch(function(response) {
        // Handle errors here, such as displaying a notification
        // for invalid email and/or password.
            $rootScope.$broadcast("app:loginError", response);
            console.error("login error", response);
        });
    }

};


})();