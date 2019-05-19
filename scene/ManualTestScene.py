from scene.SceneBase import SceneBase
from scene.SceneLayer import SceneLayer
import pygame


class ManualTestScene(SceneBase):
    def __init__(self, screen_resolution):
        self._screen_resolution = screen_resolution
        self._geometry = {}
        self._geometry[SceneLayer.BACKGROUND] = pygame.transform.scale(pygame.image.load("bg.jpg"), screen_resolution)

    def on_update(self):
        pass

    def on_render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self._geometry[SceneLayer.BACKGROUND], (0, 0))
        pygame.draw.rect(screen, (0, 128, 255),
                         pygame.Rect(0, 0.63 * screen.get_height(), screen.get_width()*0.72, 10))  # draw floor

