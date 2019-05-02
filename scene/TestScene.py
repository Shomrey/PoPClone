from scene.SceneBase import SceneBase, SceneLayer
from scene.SceneParser import SceneParser
import os
import pygame


class TestScene(SceneBase):
    def __init__(self, resolution):
        SceneBase.__init__(self, resolution)
        self.build_geometry()

    def build_geometry(self):
        filepath = 'res/scenes/test_scene.svg'
        full_path = os.path.join(os.getcwd(), filepath)
        self._geometry = SceneParser.parse(full_path, self._resolution)

    def on_render(self, screen):
        for layer, rects in self._geometry.items():
            for rect in rects:
                pygame.draw.rect(screen, rect[1], rect[0])

    def _to_screen_rect(self, rect):
        """Transforms relative-sized rect to screen sized rect"""
        return pygame.Rect(rect.x * self._resolution[0],
                           rect.y * self._resolution[1],
                           rect.width * self._resolution[0],
                           rect.height * self._resolution[1])
