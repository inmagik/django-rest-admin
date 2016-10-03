from collections import OrderedDict
from django.conf import settings
import warnings
from django.core.urlresolvers import reverse
from rest_framework import viewsets, serializers, permissions, authentication

#import logging
#logger = logging.getLogger(__name__)

#TODO:MOVE AWAY
class RestAdminConfig(object):
    serializer_class = serializers.ModelSerializer
    viewset_class = viewsets.ModelViewSet

class RestAdminRegister(object):
    """
    Holds registry for rest_admin.
    """

    def __init__(self):
        """
        #TODO: this will be lists..
        """
        self.models = OrderedDict()
        self.viewsets = OrderedDict()
        self.urls = {}


    def register(self, model, rest_admin_class=RestAdminConfig):
        """
        rest_admin_class is not used now
        it will be used to provide options (like a custom ModelAdmin class in django admin)
        """
        self.models[model._meta.object_name.lower()] = (model, rest_admin_class)


    def register_with_router(self, router):
        for v in self.models:
            model, rest_admin_class = self.models[v]

            serializer_attrs = {
                'Meta' : type('Meta', (), { 'model' : model })
            }
            serializer = type(v+'Serializer', (rest_admin_class.serializer_class,), serializer_attrs)

            viewset_attrs = {
                'serializer_class' : serializer,
                'queryset' : model.objects.all(),
                #'permission_classes' : [ permissions.IsAdminUser, ],
                #'authentication_classes' : [ authentication.TokenAuthentication, authentication.SessionAuthentication, ],
            }
            viewset = type(v+'ViewSet', (rest_admin_class.viewset_class,), viewset_attrs)
            router.register(r'%s'%v, viewset)

        return router


    def deregister(self, app_name, model):
        """
        """
        raise NotImplementedError


# Intended to be a singleton
rest_admin = RestAdminRegister()
