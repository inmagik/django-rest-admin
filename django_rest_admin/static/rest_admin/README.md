# angular-web-project

Boilerplate angular project with

- gulp
- lodash
- angular-ui-router
- restangular
- angular-http-auth
- angular-permission
- [satellizer]

## Routing

We use ui-router for routing.


## Consuming REST

This feature is based on Restangular.
#####TODO: write some boilerplate/examples for configuring rest services based on Restangular


## Autentication


angular-http-auth is used for adding an http interceptor handling 401 and 403 errors,
as well as mechanism to retry failed calls after login (#todo: link docs)

### Authentication flow

[IN PROGRESS]

Options:

* hello.js (client auth only, with support to many services and abstraction on common methods)
* **satellizer** (oauth/oauth2 support)
* ng-token-auth (similar to satellizer, with support for many events)

(For apache-cordova see:  ng-cordova-oauth)

### Use cases

* social only.





## Integration examples

?? how to handle them ? "plugins" ?




## Authorization (for local routes)

Authorization is based on angular-permissions, which integrates nicely with ui-router,
providing the concept of "permission", redirection, and events.

Config in src/config/permissions-config.js


## Combining permissions with REST: common patterns
IN PROGRESS



## Minification

Using gulp for building a "dist" folder with:
- minified css
- minified js (your source)
- js inline templates

You should write code only in the "src" folder! ** any changes made in "dist" will be overwritten by gulp. **

### Inline templates

Every .html file you put under "src/templates" folder and subfolders will be inlined 
in the `htmlTemplates` global variable. 

`htmlTemplates['relative/path/to/file.html']`



