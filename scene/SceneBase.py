from abc import ABC, abstractmethod
from scene.SceneParser import SceneParser
from scene.SceneLayer import SceneLayer
import pygame


class SceneBase(ABC):
    def __init__(self, screen_resolution, scene_file_path):
        self._screen_resolution = screen_resolution

        # contains all parsed geometry as well as the physical scene
        self._geometry = SceneParser.parse(scene_file_path, screen_resolution)

        # contains all layers to be rendered on every on_render call
        self._rendered_layers = [SceneLayer.BACKGROUND, SceneLayer.FOREGROUND]

    def on_update(self):
        pass

    @abstractmethod
    def on_render(self, screen):
        """Renders all layers stored in _rendered_layers list on the screen"""
        for layer in self._rendered_layers:
            for rect in self._geometry[layer]:
                rect.on_render(screen)

    def get_layer(self, layer):
        """
        Returns a list of rectangles representing one layer of the scene

        :param layer - SceneLayer enum class instance
        """
        return self._geometry[layer]

    def _to_screen_rect(self, rect):
        """Transforms relative-sized rect to screen sized rect"""
        return pygame.Rect(rect.x * self._screen_resolution[0],
                           rect.y * self._screen_resolution[1],
                           rect.width * self._screen_resolution[0],
                           rect.height * self._screen_resolution[1])
