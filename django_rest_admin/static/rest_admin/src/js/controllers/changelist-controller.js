(function(){
"use strict";

angular.module('app')
.controller('ChangeListCtrl', ChangeListCtrl);

function ChangeListCtrl($scope, $stateParams, DataService){
    
    $scope.name = $stateParams.name;
    var entityService  = DataService.getEntityService($scope.name)
    entityService.getList()
    .then(function(data){
        $scope.items = data;
    })

};


})();