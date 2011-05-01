# -*- coding: utf-8 -*-

from django import forms

from completeit.forms import CompleteitWidget

class TestForm(forms.Form):
    username = forms.CharField(widget=CompleteitWidget(completeit_key='u1'))