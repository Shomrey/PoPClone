class SceneBase:
    def __init__(self, resolution):
        self._resolution = resolution

    def on_update(self):
        pass

    def on_render(self, screen):
        pass

