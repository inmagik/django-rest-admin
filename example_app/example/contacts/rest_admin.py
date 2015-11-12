from django_rest_admin.register import rest_admin
from .models import Person

rest_admin.register(Person)