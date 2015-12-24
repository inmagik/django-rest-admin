(function(){
"use strict";

angular.module('app')
.controller('AddCtrl', AddCtrl);

function AddCtrl($scope, $stateParams, DataService, $state){
    
    $scope.name = $stateParams.name;  
    var entityService  = DataService.getEntityService($scope.name)
    $scope.schema = $scope.meta[$scope.name].json_schema;
    $scope.form = [
        "*",
        {
            type: "submit",
            title: "Save"
        }
    ];
    $scope.model = {};
    $scope.errors = [];

    var cleanup = function(){
        _.each($scope.errors, function(err){
            $scope.$broadcast(err[0],err[1], true);
        })
    };
    
    $scope.save = function(form){
        
        $scope.$broadcast('schemaFormValidate');
        if(!form.$valid){
            return;
        }
        
        entityService.post($scope.model)
        .then(function(resp){
            console.log(1, resp)
            var mod = resp.plain();
            $state.go("app.dashboard.changelist", {name : $scope.name})
            
        })
        .catch(function(err){
            for(var x in err.data){
                var errorEvent = 'schemaForm.error.'+x;
                console.log(1, errorEvent)
                $scope.errors.push([errorEvent,'error'])
                $scope.$broadcast(errorEvent,'error', err.data[x][0]);
            }

        })
    };
};


})();