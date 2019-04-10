from scene.SceneBase import SceneBase
import pygame


class GameScene(SceneBase):
    def __init__(self, resolution):
        SceneBase.__init__(self, resolution)
        self._background = pygame.transform.scale(pygame.image.load("bg.jpg"), resolution)

    def on_update(self):
        pass

    def on_render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self._background, (0, 0))
        pygame.draw.rect(screen, (0, 128, 255),
                         pygame.Rect(0, 0.63 * screen.get_height(), screen.get_width()*0.72, 10))  # draw floor

