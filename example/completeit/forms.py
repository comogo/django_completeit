# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings

ALLOW_AUTOCOMPLETE = getattr(settings, 'ALLOW_AUTOCOMPLETE', {})

class CompleteitWidget(forms.TextInput):
    """
    Widget used by CompleteitField.
    """
    class Media:
        js = (
            settings.MEDIA_URL + 'completeit/js/jquery.js',
            settings.MEDIA_URL + 'completeit/js/jquery-ui.js',
            settings.MEDIA_URL + 'completeit/js/completeit.js',
        )
        
        css = {
            'all': (
                settings.MEDIA_URL + 'completeit/css/jquery-ui.css',
            )
        }
    def __init__(self, completeit_key, *args, **kwargs):
        super(CompleteitWidget, self).__init__(*args, **kwargs)
        self.attrs['class'] = ' completeit'
        if not completeit_key or not ALLOW_AUTOCOMPLETE.has_key(completeit_key):
            raise ValueError('completeit_key is required but not used.')
        self.attrs['completeit_key'] = completeit_key