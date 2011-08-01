==============
django-xstatic
==============

Use XStatic_ packages and Django StaticFiles_ to manage your static
files like jQuery.

Why?
====

Managing static files is a PAIN, You must download them, unpack them copy them,
keep them up to date ...
Wouldn't it be cool if you cool just ``pip install`` them?

What does it do?
================

django-xstatic_ makes the static files from xstatic packages installed in
``INSTALLED_APPS`` be collected by ``./manage.py collectstatic``.


What it should (maybe) do, but doesn't yet
==========================================

In the current version, you still have to remember the names of the javascript
file names, but wouldn't you like to have only this in your templates::

    <head>
    {% xstatic jquery %}
    {% xstatic jquery.autocomplete %}
    </head> 

xstatic packages comes with a metadata value named LOCATIONS_, giving URLs of
CDN serving these same static files, django-xstatic should give a template tag
to use them easily.


.. _XStatic: https://bitbucket.org/thomaswaldmann/xstatic
.. _StaticFiles: https://docs.djangoproject.com/en/dev/howto/static-files/
.. _django-xstatic: http://github.com/gautier/django-xstatic
.. _LOCATIONS: http://readthedocs.org/docs/xstatic/en/latest/packaging.html#cdn-locations
