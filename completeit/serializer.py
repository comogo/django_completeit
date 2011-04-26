# -*- coding: utf-8 -*-

def completeit_serializer(format, data):
    """
    Serialize the data for completeit view.
    
    >>> completeit_serializer('json', [{'id': 1, 'value': 'item1'}, {'id': 2, 'value': 'item2'}])
    "{results: [{id:1, value:'item1'}, {id:2, value:'item2'}]}"
    
    >>> completeit_serializer('xml', ({'id': 1, 'value': 'item1'}, {'id': 2, 'value': 'item2'}))
    '<results><item><id>1</id><value>item1</value></item><item><id>2</id><value>item2</value></item></results>'
    
    >>> completeit_serializer('xmls', [{'id': 1, 'value': 'item1'}, {'id': 2, 'value': 'item2'}])
    Traceback (most recent call last):
      File "/usr/local/lib/python2.6/dist-packages/django/test/_doctest.py", line 1267, in __run
        compileflags, 1) in test.globs
      File "<doctest completeit.tests.__test__.completeit_serializer[2]>", line 1, in <module>
        completeit_serializer('xmls', [{'id': 1, 'value': 'item1'}, {'id': 2, 'value': 'item2'}])
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
        
    serialized = ''
    if format == 'json':
        serialized = "{results: [" + ", ".join(map(lambda x: "{id:%(id)s, value:'%(value)s'}" % x, data)) + "]}"
    else:
        serialized = "<results>" + "".join(map(lambda x: "<item><id>%(id)s</id><value>%(value)s</value></item>" % x, data)) + "</results>"
        
    return serialized
