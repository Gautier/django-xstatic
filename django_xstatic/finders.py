import os

from django.conf import settings
from django.contrib.staticfiles import utils
from django.contrib.staticfiles.finders import BaseFinder
from django.utils.datastructures import SortedDict

from storage import XStaticStorage

class XStaticFinder(BaseFinder):
    """
    XXX: Untested
    """
    storage_class = XStaticStorage

    def __init__(self, apps=None, *args, **kwargs):
        # The list of apps that are handled
        self.apps = []
        # Mapping of app module paths to storage instances
        self.storages = SortedDict()
        if apps is None:
            apps = settings.INSTALLED_APPS
        for app in apps:
            if app.lower().startswith('xstatic.'):
                app_storage = self.storage_class(app)
                if os.path.isdir(app_storage.location):
                    self.storages[app] = app_storage
                    if app not in self.apps:
                        self.apps.append(app)
        super(XStaticFinder, self).__init__(*args, **kwargs)

    def find(self, path, all=False):
        """
        Looks for files in the xstatic.* packages in INSTALLED_APPS
        Untested
        """
        matches = []
        for app, storage in self.storages.items():
            if storage.exists(path):
                matched_path = storage.path(path)
                if matched_path:
                    if not all:
                        return matched_path
                    matches.append(matched_path)
        return matches

    def list(self, ignore_patterns=[]):
        """
        List all files in xstatic.* packages in INSTALLED_APPS
        Untested
        """
        for app, storage in self.storages.items():
            for path in utils.get_files(storage, ignore_patterns):
                yield path, storage

