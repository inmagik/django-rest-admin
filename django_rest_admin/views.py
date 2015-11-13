from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import authentication
from django_rest_admin.register import rest_admin


def get_field_meta(field):
    """
    returns a dictionary with some metadata from field of a model
    """
    out = { 'name' : field.name, 'is_relation' : field.is_relation, 'class_name' : field.__class__.__name__}
    if field.is_relation:
        out['related_model'] = "%s.%s" % (field.related_model._meta.app_label, field.related_model.__name__)

    else:
        out['default'] = field.get_default()

    try:
        out['null'] = field.null
    except:
        pass

    return out


class RestAdminMetaView(APIView):

    authentication_classes = [ authentication.TokenAuthentication, authentication.SessionAuthentication, ]
    permission_classes = [ permissions.IsAdminUser, ]

    def get(self, request):
        out = { }
        for v in rest_admin.models:
            model = rest_admin.models[v][0]
            abs_url = request.build_absolute_uri("../"+v)
            
            fields = model._meta.get_fields(include_hidden=False)
            out_fields = []
            for field in fields:
                f = get_field_meta(field)
                out_fields.append(f)
            out[v] = {'fields' : out_fields, 'endpoint' : abs_url}

        return Response(out)
