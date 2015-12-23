(function(){
"use strict";

angular.module('app')
.controller('DetailCtrl', DetailCtrl);

function DetailCtrl($scope, $stateParams, DataService, $state){
    $scope.name = $stateParams.name;    
    $scope.id = $stateParams.id;   
    $scope.schema = $scope.meta[$scope.name].json_schema;
    $scope.form = [
        "*",
        {
            type: "submit",
            title: "Save"
        }
    ];
    $scope.model = {};

    var entityService  = DataService.getEntityService($scope.name);
    entityService.one($scope.id).get()
    .then(function(resp){
        $scope.model = resp;
    });


    $scope.save = function(form){
        $scope.$broadcast('schemaFormValidate');
        if (!form.$valid) {
            return;
        }

        $scope.model.save()
        .then(function(resp){
            var mod = resp.plain();
            _.each(mod,function(v,k){
                var errorEvent = 'schemaForm.error.'+k;
                $scope.$broadcast(errorEvent,'error', true);

            });
            $state.go("app.dashboard.changelist", {name : $scope.name})

        })
        .catch(function(err){
            for(var x in err.data){
                var errorEvent = 'schemaForm.error.'+x;
                console.log(1, errorEvent)
                $scope.$broadcast(errorEvent,'error', err.data[x][0]);
            }

        })
    };

    $scope.drop = function(){
        console.log("a", entityService.one($scope.id))
        entityService.one($scope.id).remove()
        .then(function(){
            $state.go("app.dashboard.changelist", {name : $scope.name});
        })
    }


};


})();