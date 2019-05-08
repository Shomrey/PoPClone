import pygame
from scene.render.Renderable import Renderable


class Rectangle(Renderable):
    def __init__(self, x, y, width, height, colour=(0,0,0)):
        self._rect = pygame.Rect(x, y, width, height)
        self._colour = colour       # (red, green, blue)

    def on_render(self, screen):
        pygame.draw.rect(screen, self._rect, self._colour)
