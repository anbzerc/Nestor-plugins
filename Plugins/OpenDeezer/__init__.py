from PluginCore import PluginModel
from subprocess import run

class Plugin(PluginModel):
    def run(self, must_continue_queue, text_datas_queue, plateform="flatpak"):
        if plateform == "flatpak":
            result = run("flatpak run dev.aunetx.deezer & disown %%", shell=True, timeout=10)
        must_continue_queue.put(False)
    def test(self):
        self.run()
