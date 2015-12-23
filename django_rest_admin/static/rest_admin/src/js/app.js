(function(){
"use strict";

angular.module(
    'app', 
    [   'app.constants',
        'app.networkconfig', 
        'app.statesconfig', 
        'app.permissions' ,
        'http-auth-interceptor',
        'app.satellizerconfig',
        'restangular',
        'schemaForm'
    ]
)

.run(function($rootScope){

    //hook provided by http-auth-interceptor
    
    /*
    $rootScope.$on('event:auth-loginRequired', function(event, data){
        //normally redirect to login or open a login popup
    });
    */

    // hooks provided by angular-permission
    // redirections can be handled directly in state definitions, via "redirectTo" parameter
    
    //$rootScope.$on('$stateChangePermissionStart', function(evt, toState, toParams){})
    //$rootScope.$on('$stateChangePermissionAccepted', function(evt, toState, toParams ){});
    //$rootScope.$on('$stateChangePermissionDenied', function(evt, toState, toParams){})

})


.config(function(){})




})();