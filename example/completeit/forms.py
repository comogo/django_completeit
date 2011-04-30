# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings

ALLOW_AUTOCOMPLETE = getattr(settings, 'ALLOW_AUTOCOMPLETE', {})

class CompleteitWidget(forms.TextInput):
    """
    Widget used by CompleteitField.
    """
    def __init__(self, completeit_key, *args, **kwargs):
        super(CompleteitWidget, self).__init__(*args, **kwargs)
        self.attr['class'] += ' completeit'
        if not completeit_key or not ALLOW_AUTOCOMPLETE.has_key(complete_key):
            raise ValueError('completeit_key is required but not used.')
        self.attr['completeit_key'] = completeit_key