#TODO find a better submodule name
from django.forms import widgets, fields
from django.db import models

def pretty_name(name):
    """Converts 'first_name' to 'First name'"""
    if not name:
        return u''
    return name.replace('_', ' ').capitalize()


class DjangoModelToJSONSchema(object):
    def convert_modelfield(self, name, field, json_schema):
        target_def = {
            'title': pretty_name(name),
            'description': getattr(field, 'help_text', None),
            'x-schema-form' : {}
        }
        
        if isinstance(field, models.CharField):
            target_def['type'] = 'string'
            target_def['maxlength'] = field.max_length
        elif isinstance(field, models.TextField):
            target_def['type'] = 'string'
            target_def['x-schema-form'] = {"type": "textarea"}
        if isinstance(field, models.DateField):
            target_def['type'] = 'string'
            target_def['format'] = 'date'
        elif isinstance(field, models.DateTimeField):
            target_def['type'] = 'string'
            target_def['format'] = 'datetime'
        elif isinstance(field, (models.DecimalField, models.FloatField)):
            target_def['type'] = 'number'
        elif isinstance(field, models.IntegerField):
            target_def['type'] = 'integer'
        elif isinstance(field, models.EmailField):
            target_def['type'] = 'string'
            target_def['format'] = 'email'
        elif isinstance(field, (models.NullBooleanField, models.BooleanField)):
            target_def['type'] = 'boolean'
        if isinstance(field, models.URLField):
            target_def['type'] = 'string'
            target_def['format'] = 'uri'
        else:
            target_def['type'] = 'string'


        if hasattr(field, 'choices') and field.choices:
            target_def['enum'] = [choice[0] for choice in field.choices]

        return target_def



    def convert_model(self, model, json_schema=None):
        if json_schema is None:
            json_schema = {
                #'title':dockit_schema._meta
                #'description'
                'type':'object',
                'properties':{}, #TODO SortedDict
                'required' : []
            }
        #CONSIDER: base_fields when given a class, fields for when given an instance
        fields = model._meta.get_fields(include_hidden=False)
        for field in fields:
            if isinstance(field, (models.fields.related.ManyToManyField, models.fields.reverse_related.ManyToManyRel)):
                continue

            if hasattr(field, 'primary_key') and field.primary_key:
                continue
            name = field.name
            if not field.null:
                json_schema['required'].append(name)
            json_schema['properties'][name] = self.convert_modelfield(name, field, json_schema)

        return json_schema
