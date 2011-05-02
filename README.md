Completeit
==========

Django ajax autocomplete generic app.

Installation
------------

Installation steps:

    $ git clone git://github.com/comogo/django_completeit.git
    $ cd django_completeit
    $ pyhon setup.py install
    
    done ;)

Configuration
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

Usage
-----

Use the CompleteitWidget in your form fields that you want.
You have to tell CompleteWidget completeit_key which should be used for the autocomplete.

Example:

*forms.py*:

    from django import forms
    
    from completeit.forms import CompleteitWidget

    class TestForm(forms.Form):
        username = forms.CharField(widget=CompleteitWidget(completeit_key='u1'))

*template.html*:

    <html>
      <head>
        {{ form.media }}
        <title>django_completeit example.</title>
      </head>  
      <body>
        <form method="post", action="">
          <table>
            {{ form.as_table }}
          </table>
          <input type="submit" value="Send">
        </form>
      </body>
    </html>
