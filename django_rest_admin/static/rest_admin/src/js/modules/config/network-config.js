(function(){

"use strict";

angular.module('app.networkconfig', ['restangular'])

.run(function(){})

.config(function(RestangularProvider, $httpProvider){

    /* CORS config. Affects all $http based services, included Restangular */
    /*
    $httpProvider.defaults.withCredentials = false;
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
    */
    
})

})();