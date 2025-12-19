import json


from .app_manager import AppManager
from .sidecar_manager import AppSidecarManager
from .plugin_manager import PluginManager


from mast_aladin.app import MastAladin
from jdaviz import Imviz


class MastManager():
    def __init__(self, template=None):
        self._app_manager = AppManager()
        self._plugin_manager = PluginManager(self._app_manager)
        self._sidecar_manager = AppSidecarManager(self._app_manager, self._plugin_manager)

        if template:
            self.load_from_template(template)

    def load_from_template(self, file_path):
        with open(file_path, 'r') as file:
            template = json.load(file)
        
        app_template = template['apps']
        for app in app_template:
            if app["type"] == "MastAladin":
                self._app_manager.register_app(MastAladin(), app["name"])
            if app["type"] == "Imviz":
                self._app_manager.register_app(Imviz(), app["name"])

        sidecar_template = template["sidecars"]
        for sidecar in sidecar_template:
            apps = [app for idx, app in self.apps.items() if idx in sidecar["apps"]]
            self._sidecar_manager.open_single(
                apps=apps,
                ref=sidecar.get("ref", None),
                title=sidecar["title"],
                anchor=sidecar["anchor"]
            )
        self.open_plugins()

        # self._sidecar_manager.temp(
        #     apps=,
        #     title="plugins",
        #     anchor="right"
        # )

    @property
    def AppManager(self):
        return self._app_manager

    @property
    def apps(self):
        return self._app_manager.apps

    @property
    def UiManager(self):
        return self._ui_manager

    @property
    def SidecarManager(self):
        return self._sidecar_manager

    @property
    def PluginManager(self):
        return self._plugin_manager

    @property
    def plugins(self):
        return self._plugin_manager.plugins

    def register_app(self, app, idx):
        self._app_manager.register_app(app, idx)

    def open_sidecar(self):
        self._sidecar_manager.open()

    def open_plugins(self):
        self._plugin_manager.display_all_plugins()

    def open(self):
        self.open_sidecar()
        self.open_plugins()
