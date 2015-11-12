"""
* standard urls
    * authentication endpoints
    * metadata endpoints 
* urls coming from registered models
"""

from django.conf.urls import patterns, include, url
from .views import RestAdminMetaView
from .register import rest_admin
from rest_framework import routers


urlpatterns = patterns('',
     url(r'^meta/$', RestAdminMetaView.as_view(), name='rest_admin_meta'),
     #url(r'^login/$', ModelsMetaView.as_view(), name='login'),
)

router = routers.SimpleRouter()

slizers = {}
vsets = {}

router = rest_admin.register_with_router(router)

urlpatterns += router.urls
