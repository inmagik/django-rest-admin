from django_rest_admin.register import rest_admin
from .models import Person, Place

rest_admin.register(Person)
rest_admin.register(Place)