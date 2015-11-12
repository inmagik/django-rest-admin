=============================
django-rest-admin
=============================

.. image:: https://badge.fury.io/py/django-rest-admin.png
    :target: https://badge.fury.io/py/django-rest-admin

.. image:: https://travis-ci.org/inmagik/django-rest-admin.png?branch=master
    :target: https://travis-ci.org/inmagik/django-rest-admin

REST endpoints for administering django models.

Documentation
-------------

The full documentation is at https://django-rest-admin.readthedocs.org.

Quickstart
----------

Install django-rest-admin::

    pip install django-rest-admin

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
