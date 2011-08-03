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

Installation and usage
======================

    1. Install django-xstatic
    2. Add ``'django_xstatic.finders.XStaticFinder'`` to your ``STATICFILES_FINDERS``
    2. Install your xstatic packages and add them to ``INSTALLED_APPS``
    3. run ``./manage.py collectstatic``

Open questions
==============

django-xstatic detects xstatic package when they are in the ``INSTALLED_APPS``
list. Should it uses its own settings key?


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

Bonus Feature
=============

It works with django-compressor_!

.. _XStatic: https://bitbucket.org/thomaswaldmann/xstatic
.. _StaticFiles: https://docs.djangoproject.com/en/dev/howto/static-files/
.. _django-xstatic: http://github.com/gautier/django-xstatic
.. _LOCATIONS: http://readthedocs.org/docs/xstatic/en/latest/packaging.html#cdn-locations
.. _django-compressor: http://django_compressor.readthedocs.org/
