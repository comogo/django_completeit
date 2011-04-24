# -*- coding: utf-8 -*-
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.conf import settings


class AutocompleteTeste(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='test1', email='test1@test.com')
        User.objects.create(username='test2', email='test2@test.com')
        User.objects.create(username='user1',  email='user1@test.com')
        settings.ALLOW_AUTOCOMPLETE = {
            'auth.User': ['username']
        }
        
    def test_autocomplete_field_fail(self):
        """
        Try autocomplete field not allowed.
        """
        response = self.client.get('/autocomplete/?m=auth.User&f=email&r=name&q=test')
        self.assertEqual(response.content, '{}')

    def test_autocomplete_pass(self):
        """
        Pass the test.
        """
        response = self.client.get('/autocomplete/?m=auth.User&f=username&r=username&q=test')
        self.assertContains(response, 'test1')
