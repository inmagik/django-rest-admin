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
        templateUrl: 'templates/home.html'
    })

    .state('app.dashboard.changelist', {
        url: '/changelist/:name',
        cache: false,
        templateUrl: 'templates/changelist.html',
        controller: 'ChangeListCtrl'
        
    })

    .state('app.dashboard.detail', {
        url: '/detail/:name/:id',
        cache: false,
        templateUrl: 'templates/detail.html',
        controller: 'DetailCtrl'
        
    })

    .state('app.dashboard.add', {
        url: '/add/:name',
        cache: false,
        templateUrl: 'templates/new.html',
        controller: 'AddCtrl'
    });

    $urlRouterProvider.otherwise(function ($injector) {
        var $state = $injector.get('$state');
        $state.go('app.dashboard.home');
    });

})

})();