import pygame
from scene.render.Renderable import Renderable


class Rectangle(Renderable):
    def __init__(self, x, y, width, height, colour=(0,0,0), scale_x=1, scale_y=1):
        # x *= scale_x
        # width *= abs(scale_x)
        # if scale_x < 0:
        #     x -= width
        # y *= abs(scale_y)
        # height *= scale_y
        # if scale_y < 0:
        #     y += height
        self._rect = pygame.Rect(x, y, width, height)
        self._colour = colour       # (red, green, blue)

    def on_render(self, screen, screenshot_resolution, screenshot_x_offset):
        pygame.draw.rect(screen, self._colour, Renderable.to_screen_rect(self._rect, screen.get_rect(), screenshot_resolution, screenshot_x_offset))

    def get_x(self):
        return self._rect.x

    def get_y(self):
        return self._rect.y

    def get_rect(self):
        return self._rect

