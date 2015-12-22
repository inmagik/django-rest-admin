(function(){
"use strict";

angular.module('app')
.controller('AppCtrl', AppCtrl);

function AppCtrl($scope, $auth, $rootScope){
    
    $scope.logged = $auth.isAuthenticated();
    $scope.$on("app:loginSuccess", function(){
        $scope.logged = true;
    });
    $scope.logout = function(){
        $auth.logout()
        $rootScope.$broadcast("app:logoutSuccess");
        $scope.logged = false;
    };
};


})();