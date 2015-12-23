(function(){

"use strict";

angular.module('app.statesconfig', ['ui.router'])

.run(function($rootScope, $state){

    //perform redirects based on login/logout here
    
    $rootScope.$on("app:logoutSuccess", function(){
        $state.go("app.login");
    });

    $rootScope.$on("app:loginSuccess", function(){
        $state.go("app.dashboard.home");
    });
    

})

.config(function($stateProvider, $urlRouterProvider){

    /* States config */

    $stateProvider
    .state('app', {
        url: '/app',
        abstract: true,
        template : '<ui-view></ui-view>',
        //controller : 'RootCtrl'
    })
    .state('app.login', {
        url: '/login',
        templateUrl: 'templates/login.html',
        controller: 'LoginCtrl',
        data: {
            permissions: {
                except: ['logged'],
                redirectTo: 'app.dashboard.home'
            },

        },
    })
    /*
    .state('app.account', {
        url: '/account',
        templateUrl: 'templates/account.html',
        //controller: 'AccountCtrl',
        resolve: {
          
        },
        data: {
            permissions: {
                except: ['anonymous'],
                redirectTo: 'app.login'
            },

        },
    })
    */
    .state('app.dashboard', {
        url: '/dashboard',
        abstract : true,
        templateUrl: 'templates/dashboard.html',
        controller: function($scope, meta){
            $scope.meta = meta.plain();
            console.log(1, $scope.meta);
        },
        resolve: {
            meta : function(DataService){
                return DataService.restMeta.get()
            }
          
        },
        
        data: {
            permissions: {
                only: ['logged'],
                redirectTo: 'app.login'
            }
        }
        
    })

    .state('app.dashboard.home', {
        url: '',
        templateUrl: 'templates/home.html',
        data: {
            permissions: {
                only: ['logged'],
                redirectTo: 'app.login'
            }
        }
        
    })

    .state('app.dashboard.changelist', {
        url: '/changelist/:name',
        templateUrl: 'templates/changelist.html',
        controller: function($scope, $stateParams){
            $scope.name = $stateParams.name;
        },
        resolve: {
            
        },
        
        data: {
            permissions: {
                only: ['logged'],
                redirectTo: 'app.login'
            }
        }
        
    })

    .state('app.dashboard.detail', {
        url: '/detail/:name',
        templateUrl: 'templates/detail.html',
        controller: function($scope, $stateParams){
          $scope.name = $stateParams.name;  
        },
        resolve: {
            
        },
        
        data: {
            permissions: {
                only: ['logged'],
                redirectTo: 'app.login'
            }
        }
        
    })

    .state('app.dashboard.add', {
        url: '/add/:name',
        templateUrl: 'templates/new.html',
        controller: function($scope, $stateParams, DataService){

          $scope.name = $stateParams.name;  
          $scope.schema = $scope.meta[$scope.name].json_schema;
          $scope.form = [
            "*",
            {
              type: "submit",
              title: "Save"
            }
          ];
          $scope.model = {};
          $scope.save = function(){
            console.log(100, $scope.model);
          };

          
        },
        resolve: {
            
        },
        
        data: {
            permissions: {
                only: ['logged'],
                redirectTo: 'app.login'
            }
        }
        
    });

    $urlRouterProvider.otherwise(function ($injector) {
        var $state = $injector.get('$state');
        $state.go('app.dashboard.home');
    });

})

})();