# -*- coding: utf-8 -*-
from django.utils import simplejson

def completeit_serializer(format, data):
    """
    Serialize the data for completeit view.
    
    >>> from django.utils import simplejson
    >>> params = [{'label': 1, 'value': 'item1'}, {'label': 2, 'value': 'item2'}]
    >>> ser = completeit_serializer('json', params)
    >>> simplejson.loads(ser) == {'results': params}
    True
    
    >>> completeit_serializer('xml', params)
    '<results><item><label>1</label><value>item1</value></item><item><label>2</label><value>item2</value></item></results>'
    
    >>> completeit_serializer('xmls', [{'label': 1, 'value': 'item1'}, {'label': 2, 'value': 'item2'}])
    Traceback (most recent call last):
      File "/usr/local/lib/python2.6/dist-packages/django/test/_doctest.py", line 1267, in __run
        compileflags, 1) in test.globs
      File "<doctest completeit.tests.__test__.completeit_serializer[2]>", line 1, in <module>
        completeit_serializer('xmls', [{'label': 1, 'value': 'item1'}, {'label': 2, 'value': 'item2'}])
      File "/home/mateus.santos/projects/django_completeit/example/completeit/serializer.py", line 32, in completeit_serializer
        raise ValueError('xml or json expected in format.')
    ValueError: xml or json expected in format.
    
    >>> completeit_serializer('xml', 'test')
    Traceback (most recent call last):
      File "/usr/local/lib/python2.6/dist-packages/django/test/_doctest.py", line 1267, in __run
        compileflags, 1) in test.globs
      File "<doctest completeit.tests.__test__.completeit_serializer[3]>", line 1, in <module>
        completeit_serializer('xml', 'test')
      File "/home/mateus.santos/projects/django_completeit/example/completeit/serializer.py", line 24, in completeit_serializer
        raise ValueError('data is not a list or tuple.')
    ValueError: data is not a list or tuple.
    """
    if not (isinstance(data, list) or isinstance(data, tuple)):
        raise ValueError('data is not a list or tuple.')
    
    if format not in ('xml', 'json'):
        raise ValueError('xml or json expected in format.')
        
    if format == 'json':
        #return '{"results": [' + ", ".join(map(lambda x: '{"label":"%(label)s", "value":"%(value)s"}' % x, data)) + "]}"
        return simplejson.dumps({'results': data})
    else:
        return "<results>" + "".join(map(lambda x: "<item><label>%(label)s</label><value>%(value)s</value></item>" % x, data)) + "</results>"