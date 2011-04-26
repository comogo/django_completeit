# -*- coding: utf-8 -*-
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from completeit.serializer import completeit_serializer

class CompleteitTest(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create(username='test1', email='test1@test.com')
        User.objects.create(username='test2', email='test2@test.com')
        User.objects.create(username='user1',  email='user1@test.com')

    def test_completeit_pass(self):
        """
        Test usually use without specifying the format..
        """
        response = self.client.get('/completeit/?k=u1&q=test')
        self.assertEquals(response.content, "{results: [{id:1, value:'test1'}, {id:2, value:'test2'}]}")
            
    def test_completeit_json_pass(self):
        """
        Testing usually use the JSON format.
        """
        response = self.client.get('/completeit/?k=u1&q=test&f=json')
        self.assertEquals(response.content, "{results: [{id:1, value:'test1'}, {id:2, value:'test2'}]}")
        
    def test_completeit_xml_pass(self):
        """
        Testing usually use the XML format.
        """
        response = self.client.get('/completeit/?k=u1&q=test&f=xml')
        self.assertEquals(response.content, "<results><item><id>1</id><value>test1</value></item><item><id>2</id><value>test2</value></item></results>")

    def test_completeit_key_fail(self):
        """
        Testing autocomplete for a key not defined in ALLOW_AUTOCOMPLETE settings.
        """
        response = self.client.get('/completeit/?k=u2&q=test')
        self.assertEqual(response.content, '{results: []}')
    
    def test_completeit_key_fail_xml(self):
        """
        Testing autocomplete for a key not defined in ALLOW_AUTOCOMPLETE settings specifying XML format.
        """
        response = self.client.get('/completeit/?k=u2&q=test&f=xml')
        self.assertEqual(response.content, '<results></results>')

    def test_completeit_query_fail(self):
        """
        Testing autocomplete without query.
        """
        response = self.client.get('/completeit/?k=u1')
        self.assertEqual(response.content, '{results: []}')

    def test_completeit_key_query_fail(self):
        """
        Testing autocomplete for a key not defined in ALLOW_AUTOCOMPLETE settings without query.
        """
        response = self.client.get('/completeit/?k=u2')
        self.assertEqual(response.content, '{results: []}')

__test__ = {
    'completeit_serializer': completeit_serializer,
}
