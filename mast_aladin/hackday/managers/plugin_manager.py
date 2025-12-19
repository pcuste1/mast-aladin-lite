from mast_aladin.hackday.adapters import ViewerSync, ViewportOutlinePlugin
from IPython.display import display


class PluginManager():
    def __init__(self, app_manager):
        self._plugins = {
            "viewer_sync": ViewerSync(app_manager),
            # "viewport_outline": ViewportOutlinePlugin(app_manager)
        }

    @property
    def plugins(self):
        return self._plugins

    def display_plugin(self, idx):
        self._plugins[idx].display()

    def display_all_plugins(self):
        for idx in self._plugins:
            self.display_plugin(idx)
