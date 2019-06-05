import pygame
from scene.render.Renderable import Renderable


class Image(Renderable):
    def __init__(self, x, y, width, height, filepath, scale_x=1, scale_y=1, clip_rect=None):
        self._image = pygame.image.load(filepath)
        if scale_x < 0:
            self._image = pygame.transform.flip(self._image, True, False)
            x = abs(x + width)
        if scale_y < 0:
            self._image = pygame.transform.flip(self._image, False, True)
        self._rect = pygame.rect.Rect(x, y, width, height)
        if clip_rect:
            self._rect = self._rect.clip(clip_rect)

    def on_render(self, screen, screenshot_resolution, screenshot_x_offset):
        rect = Renderable.to_screen_rect(self._rect, screen.get_rect(), screenshot_resolution, screenshot_x_offset)
        image = pygame.transform.scale(self._image, (rect.width, rect.height))
        screen.blit(image, rect)
