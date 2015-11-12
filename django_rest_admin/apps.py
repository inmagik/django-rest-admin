from django.apps import AppConfig
from django.conf import settings

import sys
import imp
import importlib
import os
 

class RestAdminAppConfig(AppConfig):

    name = 'django_rest_admin'
    verbose_name = 'Rest Admin'
    loaded = False
 
    def ready(self):
        autodiscover()
        

def autodiscover():
    """
    Automatic discovering of rest_admin.py file inside apps.
    similar to what Django admin does. 
    """
    if not RestAdminAppConfig.loaded:
        for app in settings.INSTALLED_APPS:
            # For each app, we need to look for an rest_admin.py inside that app's
            # package. We can't use os.path here -- recall that modules may be
            # imported different ways (think zip files) -- so we need to get
            # the app's __path__ and look for rest_admin.py on that path.

            # Step 1: find out the app's __path__ Import errors here will (and
            # should) bubble up, but a missing __path__ (which is legal, but weird)
            # fails silently -- apps that do weird things with __path__ might
            # need to roll their own rest_admin registration.
            try:
                app_path = importlib.import_module(app).__path__
            except AttributeError:
                continue

            # Step 2: use imp.find_module to find the app's rest_admin.py. For some
            # reason imp.find_module raises ImportError if the app can't be found
            # but doesn't actually try to import the module. So skip this app if
            # its rest_admin.py doesn't exist
            try:
                imp.find_module('rest_admin', app_path)
            except ImportError:
                continue

            # Step 3: import the app's admin file. If this has errors we want them
            # to bubble up.
            importlib.import_module("%s.rest_admin" % app)
        
        # autodiscover was successful, reset loading flag.
        RestAdminAppConfig.loaded = True
                    