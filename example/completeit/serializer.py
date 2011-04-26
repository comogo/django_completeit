# -*- coding: utf-8 -*-

def completeit_serializer(format, data):
    """
    Serialize the data for completeit view.
    
    >>> completeit_serializer('json', ['item1', 'item2'])
    "results: ['item1', 'item2']"
    
    >>> completeit_serializer('xml', ('item1', 'item2'))
    '<results><item>item1</item><item>item2</item></results>'
    
    >>> completeit_serializer('xmls', ['item1', 'item2'])
    Traceback (most recent call last):
    ValueError xml or json expected in format.
    
    >>> completeit_serializer('xml', 'test')
    Traceback (most recent call last):
    ValueError data is not a list or tuple.
    """
    if not (isinstance(data, list) or isinstance(data, tuple)):
        raise ValueError('data is not a list or tuple.')
    
    if format not in ('xml', 'json'):
        raise ValueError('xml or json expected in format.')
        
    serialized = ''
    new_list = map(lambda x: "'%s'" % x, data)
    if format == 'json':
        serialized = "{results: [" + ", ".join(new_list) + "]}"
    else:
        serialized = "<results>" + "".join(map(lambda x: "<item>"+ x +"</item>", data)) + "</results>"
        
    return serialized