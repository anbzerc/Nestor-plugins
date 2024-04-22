from PluginCore import PluginModel
from subprocess import run

class Plugin(PluginModel):
    def run(self, plateform="flatpack"):
        if plateform == "flatpak":
            result = run("flatpak run dev.aunetx.deezer & disown %%", shell=True, timeout=10)

    def test(self):
        self.run()
