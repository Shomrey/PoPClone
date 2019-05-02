from collections import defaultdict
from enum import Enum


class SceneLayer(Enum):
    PHYSICAL_SCENE = 1


class SceneBase:
    def __init__(self, resolution):
        self._resolution = resolution
        self._geometry = defaultdict(lambda: [])     # contains all parsed geometry

    def on_update(self):
        pass

    def on_render(self, screen):
        pass

    def get_layer(self, layer):
        """
        Returns a list of rectangles representing one layer of the scene

        :param layer - SceneLayer enum class instance
        """
        return self._geometry[layer]
