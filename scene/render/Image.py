import pygame
from scene.render.Renderable import Renderable


class Image(Renderable):
    def __init__(self, x, y, width, height, filepath):
        self._image = pygame.image.load(filepath)
        self._rect = pygame.rect.Rect(x, y, width, height)

    def on_render(self, screen):
        screen.blit(self._image, self._rect)
