=============================
django-rest-admin
=============================

THIS PROJECT IS IN AN EARLY STAGE, DO NOT USE IN PRODUCTION, IT LACKS MOST OF THE BASIC FEATURES - MOST NOTABLY SECURITY FEATURES.

django-rest-admin is a django reusable app that aims at providing an easy way to create rest endpoints for managing model instances, pretty much like the admin does.

* automatic urls configuration
* simple registration of models via autodiscovering
* metadata about models and endpoints

This app is based on django-rest-framework.


Quickstart
----------

Install django-rest-admin::

    python setup.py install


Then use it in a project:

Attach rest_admin urls in your main `urls.py` file::

    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^rest_admin/', include('django_rest_admin.urls')),
    ]


You can then register a model in a file named `rest_admin.py` just like::

    from django_rest_admin.register import rest_admin
    from .models import Person

    rest_admin.register(Person)


Now navigate to the url you used for hooking up rest_admin:

    http://localhost:8000/rest_admin/

You should be taken to your new admin interface, based on angular js. 


How it works
------------
When you register a model, builds a REST-style CRUD interface by:

* creating a django-rest-framework `ModelViewSet` class and passing in a `ModelSerializer` 
* mounting the viewset urls

Additionally, `rest_admin` creates a `meta` endpoint that exposes all configuration for registered models, that should include:

* base REST endpoint for that model
* model fields definition 
* json-schema of the model

Given this metadata is possible to build a client application acting as an admin.

The project bundles an angular 1.x based admin. This frontend will eventually moved to another project and become an example on how to build apps using the REST interface provided by this project.


Features
--------

* model registration à la admin (basic and non customizable for now)
* automatic rest endpoint generation
* experimental angular frontend


Ideas
-----

* Use the same approach to generate read-only endpoints. This would be useful for applications that only need to display or search data without modifying it.


