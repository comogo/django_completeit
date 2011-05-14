from setuptools import setup
 
version = '0.0.1'
 
LONG_DESCRIPTION = """
=====================================
django_completeit (Django completeit)
=====================================

"""
 
setup(
    name='completeit',
    version=version,
    description="django_completeit",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='ajax,django,autocomplete',
    author='Mateus Lorandi dos Santos',
    author_email='mcomogo@gmail.com',
    license='MIT',
    packages=['completeit'],
    url='http://github.com/comogo/django_completeit',
    include_package_data=True,
    exclude_package_data={'': ['example']},
    zip_safe=False,
)
