from abc import ABC, abstractmethod
from scene.SceneParser import SceneParser
from scene.SceneLayer import SceneLayer
import pygame


class SceneBase(ABC):
    def __init__(self, screen_resolution, scene_file_path):
        self._screen_resolution = screen_resolution

        # contains all parsed geometry as well as the physical scene
        self._geometry, scene_resolution = SceneParser.parse(scene_file_path)
        screenshot_width = self.get_layer(SceneLayer.SCREEN_BORDERS)[1].get_x() - self.get_layer(SceneLayer.SCREEN_BORDERS)[0].get_x()  # TODO: Handle uneven screenshots
        self._screenshot_resolution = (screenshot_width, scene_resolution[1])
        self._current_screenshot = self.get_screenshot_number(self.get_layer(SceneLayer.START_POSITION)[0].get_x())

        # contains all layers to be rendered on every on_render call
        self._rendered_layers = [SceneLayer.BACKGROUND, SceneLayer.FOREGROUND]

    def on_update(self):
        pass

    @abstractmethod
    def on_render(self, screen):
        """Renders all layers stored in _rendered_layers list on the screen"""
        # screenshot_number = self.get_screenshot_number(player_position.x)

        for layer in self._rendered_layers:
            for rect in self._geometry[layer]:
                rect.on_render(screen, self._screenshot_resolution, self._screenshot_resolution[0] * self._current_screenshot)

    def get_layer(self, layer):
        """
        Returns a list of rectangles representing one layer of the scene

        :param layer - SceneLayer enum class instance
        """
        return self._geometry[layer]

    def get_screenshot_number(self, x):
        return x // self._screenshot_resolution[0]
