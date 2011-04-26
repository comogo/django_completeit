# -*- coding: utf-8 -*-
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class AutocompleteTeste(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='test1', email='test1@test.com')
        User.objects.create(username='test2', email='test2@test.com')
        User.objects.create(username='user1',  email='user1@test.com')
        
    def test_autocomplete_key_fail(self):
        """
        Try autocomplete field not allowed.
        """
        response = self.client.get('/completeit/?k=u2&q=test')
        self.assertEqual(response.content, '{results: []}')

    def test_autocomplete_pass(self):
        """
        Pass the test.
        """
        response = self.client.get('/completeit/?k=u1&q=test')
        self.assertEquals(response.content, "{results: ['test1', 'test2']}")
        
    def test_autocomplete_xml(self):
        """
        Teste xml response.
        """
        response = self.client.get('/completeit/?k=u1&q=test&f=xml')
        self.assertEquals(response.content, "<results><item>test1</item><item>test2</item></results>")