from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'completeit.views.autocomplete', name='completeit'),
)
