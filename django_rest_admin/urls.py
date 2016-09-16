"""
* standard urls
    * authentication endpoints
    * metadata endpoints
* urls coming from registered models
"""

from django.conf.urls import patterns, include, url
from django.conf import settings
from .views import RestAdminMetaView
from .register import rest_admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

#TODO: login/logout views disabled by settings

urlpatterns = [
    # probably would be better to provide our own endpoints.
    url(r'^session-login/', auth_views.login),
    url(r'^session-logout/', auth_views.logout),
    url(r'^token-login/', obtain_auth_token),
    url(r'^meta/$', RestAdminMetaView.as_view(), name='rest_admin_meta')
]

router = rest_admin.register_with_router(routers.SimpleRouter())
urlpatterns += router.urls
