from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage
from django.utils.importlib import import_module


class XStaticStorage(FileSystemStorage):
    """
    A file system storage backend that takes an xstatic package module and works
    for the data contained in it.
    """
    prefix = None

    def __init__(self, package, *args, **kwargs):
        """
        Returns a static file storage if available in the given xstatic package
        """
        module, attr = package.rsplit('.', 1)
        try:
            mod = import_module(module)
        except ImportError, e:
            raise ImproperlyConfigured('Error importing module %s: "%s"' %
                                       (module, e))
        try:
            package = getattr(mod, attr)
        except AttributeError:
            raise ImproperlyConfigured('Module "%s" does not contains a "%s" '
                                       'package.' % (module, attr))
        location = package.BASE_DIR
        super(XStaticStorage, self).__init__(location, *args, **kwargs)

