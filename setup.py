from setuptools import setup, find_packages
 
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
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)