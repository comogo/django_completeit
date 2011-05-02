Completeit
==========

Django ajax autocomplete generic app.

Installation
------------

Add the 'completeit' directory somewhere on your 'PYTHONPATH', put it into 'INSTALLED_APPS' in your settings file.
Fill in your ALLOW_AUTOCOMPLETE in your settings file, like this:

    ALLOW_AUTOCOMPLETE = {
        'completeit_key': {
            'model': 'app.Model',
            'search': ('field__lookup',),
            'label': 'field_name',
            'value': 'field_name'
        }
    }

Add the bellow settings to your URLconf:

    urlpatterns = patterns('',
        ...
        (r'^completeit/', include('completeit.urls')),
    )

Copy the content of completeit media folder or create a symlink to your media:

    ln -s /path/to/your/completeit/media/completeit /path/to/your/media/
