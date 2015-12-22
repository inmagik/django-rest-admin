(function(){
"use strict";

angular.module('app.satellizerconfig', ['satellizer'])

.config(function ($authProvider) {
  /* configuring satellizer for working with django rest framework token auth */
  $authProvider.baseUrl = '/rest_admin';
  $authProvider.loginUrl = '/token-login/';
  $authProvider.authToken = 'Token';
});

})();