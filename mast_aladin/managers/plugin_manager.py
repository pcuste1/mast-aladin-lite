from mast_aladin.adapters import ViewerSyncPlugin


class PluginManager():
    def __init__(self, mast_manager):
        self._plugins = {
            "viewer_sync": ViewerSyncPlugin(mast_manager.AppManager),
        }

    @property
    def plugins(self):
        return self._plugins

    def display_plugin(self, id):
        self._plugins[id].display()

    def display_all_plugins(self):
        for id in self._plugins:
            self.display_plugin(id)
