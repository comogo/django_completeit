Installation
============

Clone the repository then execute::
    python setup.py install

Add *'compleit'* to your INSTALLED_APPS in settings.py::
    INSTALLED_APPS = {
      ...
      'completeit',
    }
    

Settings
========

Models and fields allowed to autocomplete in settings.py::
    ALLOW_AUTOCOMPLETE = {
      'module.Model': ['field_allowed'],
    }

Ex::
    ALLOW_AUTOCOMPLETE = {
      'auth.User': ['username', 'email'],
    }