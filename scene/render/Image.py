import pygame
from scene.render.Renderable import Renderable


class Image(Renderable):
    def __init__(self, x, y, width, height, filepath, scale_x=1, scale_y=1, clip_rect=None):
        self._image = pygame.image.load(filepath)

        x *= scale_x
        width *= abs(scale_x)
        if scale_x < 0:
            x -= width
            self._image = pygame.transform.flip(self._image, True, False)

        y *= abs(scale_y)
        height *= scale_y
        if scale_y < 0:
            y += height
            self._image = pygame.transform.flip(self._image, False, True)
        self._rect = pygame.rect.Rect(x, y, width, height)

        if clip_rect:
            original_rect = self._rect.copy()
            self._rect = self._rect.clip(clip_rect)

            # crop the image
            image_scale_x = self._image.get_width() / original_rect.width
            image_scale_y = self._image.get_height() / original_rect.height
            crop_area_width = self._rect.width * image_scale_x
            crop_area_height = self._rect.height * image_scale_y
            crop_area_x = (self._rect.x - original_rect.x) * image_scale_x
            crop_area_y = (self._rect.y - original_rect.y) * image_scale_y

            crop_area = (crop_area_x, crop_area_y, crop_area_width, crop_area_height)
            cropped_image = pygame.Surface((crop_area_width, crop_area_height))
            cropped_image.blit(self._image, (0, 0), crop_area)
            self._image = cropped_image

    def on_render(self, screen, screenshot_resolution, screenshot_x_offset):
        rect = Renderable.to_screen_rect(self._rect, screen.get_rect(), screenshot_resolution, screenshot_x_offset)
        image = pygame.transform.scale(self._image, (rect.width, rect.height))
        screen.blit(image, rect)
