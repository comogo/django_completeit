# -*- coding: utf-8 -*-
# ALLOW_AUTOCOMPLETE is a dict of list.
#
# Ex: ALLOW_AUTOCOMPLETE_TO = {
#        'auth.User': ('username', 'first_name',),
#        'flatpages.FlatPage': ('title',)
#     }
#
from django.views.decorators.http import require_http_methods
from django.db.models.loading import get_model
from django.utils import simplejson
from django.http import HttpResponse
from django.conf import settings

ALLOW_AUTOCOMPLETE = getattr(settings, 'ALLOW_AUTOCOMPLETE', [])

@require_http_methods(["GET"])
def autocomplete(request):
    """
    Response only for GET method.
    Look for itens in queryset:
        - m (Model name) Ex: app.Model
        - f (Field to search)
        - q (Data)
        - r (Field returned)
        
    Return a list 
    """
    data = {}
    if 'm' in request.GET and 'f' in request.GET and 'q' in request.GET and 'r' in request.GET:
        try:
            model_path = request.GET.get('m')
            field = request.GET.get('f')
            q = request.GET.get('q')
            r = request.GET.get('r')
            
            if ALLOW_AUTOCOMPLETE.has_key(model_path):
                if field in ALLOW_AUTOCOMPLETE.get(model_path):
                    app_name, model_name = model_path.split('.')
                    model = get_model(app_name, model_name)
                    lookup = {'%s__istartswith' % field: q}
                    qs = model.objects.filter(**lookup).values(r)
                    data = {'result': [ d.get(r) for d in qs ]}
        except ValueError:
            pass
            
    return HttpResponse(simplejson.dumps(data), mimetype='application/json')