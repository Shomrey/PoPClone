from scene.SceneBase import SceneBase
import pygame


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def on_update(self):
        pass

    def on_render(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 200, screen.get_width(), 10))  # draw floor

