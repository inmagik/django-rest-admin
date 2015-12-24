from django_rest_admin.register import rest_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

rest_admin.register(get_user_model())
rest_admin.register(Group)
