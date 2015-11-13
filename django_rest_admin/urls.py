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
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # probably would be better to provide our own endpoints.
    url(r'^session-login/', auth_views.login),
    url(r'^session-logout/', auth_views.logout),
    url(r'^token-login/', 'rest_framework.authtoken.views.obtain_auth_token'),
    
    url(r'^meta/$', RestAdminMetaView.as_view(), name='rest_admin_meta'),
)

router = rest_admin.register_with_router(routers.SimpleRouter())
urlpatterns += router.urls
