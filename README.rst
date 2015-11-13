=============================
django-rest-admin
=============================

THIS PROJECT IS IN AN EARLY STAGE, DO NOT USE IN PRODUCTION, IT LACKS MOST OF THE BASIC FEATURES.


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

Features
--------

* TODO
