# -*- coding: utf-8 -*-
"""
ALLOW_AUTOCOMPLETE is a dict of list.
Ex:
ALLOW_AUTOCOMPLETE_TO = {
    'u1': {
        'model': 'auth.User',
        'lookup_fields': ('username__istartswith', 'first_name__istartswith',),
        'return': 'username' # Field of model,
        'format': 'json' # optional
    },
    'f1': {
        'model': 'flatpages.FlatPage',
        'lookup_fields': ('title__icontains',),
        'return': 'title',
        'format': 'json' # optional
    }
}
"""
from django.views.decorators.http import require_http_methods
from django.db.models.loading import get_model
from django.db.models import Q
from django.http import HttpResponse
from django.conf import settings

from completeit.serializer import completeit_serializer

ALLOW_AUTOCOMPLETE = getattr(settings, 'ALLOW_AUTOCOMPLETE', {})

@require_http_methods(["GET"])
def completeit(request):
    """
    Response only for GET method.
    Look for itens in queryset:
        - k (key)
        - q (Data)
        - f (format) JSON/XML
    Return:
        - List (JSON/XML) default (JSON)
    
    /completeit/?k=u1&q=admin&f=JSON
    /completeit/?k=u1&q=admin&f=XML
    /completeit/?k=u1&q=admin
    """
    format= request.GET.get('f', 'json').lower()
    if format not in ('json', 'xml'):
        return HttpResponse('')
    data = []
    if 'k' in request.GET and 'q' in request.GET:
        query = request.GET.get('q')
        key = request.GET.get('k')
        
        if ALLOW_AUTOCOMPLETE.has_key(key):
            completeit_key =  ALLOW_AUTOCOMPLETE.get(key)
            app_name, model_name = completeit_key.get('model').split('.')
            model = get_model(app_name, model_name)                
            lookup = None
            for i, l in enumerate(completeit_key.get('lookup_fields')):
                if i == 0:
                    lookup = Q(**{l: query})
                else:
                    lookup |= Q(**{l: query})
                    
            field = completeit_key.get('return')
            qs = model.objects.filter(lookup).values('pk', field)
            data = [ {'id': d.get('pk'), 'value': d.get(field)} for d in qs ]
    
    serialized_data = completeit_serializer(format, data)
    return HttpResponse(serialized_data, mimetype='application/%s' % format)
