(function(){
"use strict";

angular.module('app.permissions', ['permission', 'satellizer'])

.run(function (Permission, $rootScope, $auth) {
  
  Permission.defineRole('logged', function () {
    return $auth.isAuthenticated()
  });

});

})();