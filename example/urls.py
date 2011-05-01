from django.conf.urls.defaults import *
from django.conf import settings

from app.forms import TestForm

urlpatterns = patterns('',
    ('^$', 'django.views.generic.simple.direct_to_template',
            {
                'template': 'index.html',
                'extra_context': {
                    'form': TestForm()
                }
            }),
    ('^completeit/', include('example.completeit.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
)
