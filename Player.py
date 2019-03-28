import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._position = [20, 210]
        self._sprite_size = [50, 70]
        self._image = pygame.transform.scale(pygame.image.load("player.jpg"), self._sprite_size)

    def on_update(self):
        pass

    def on_render(self, screen):
        position_rect = self._image.get_rect().move(self._position[0], self._position[1])
        screen.blit(self._image, position_rect)

    def get_position(self):
        return self._position

    def set_position(self, x, y):
        if x is not None:
            self._position[0] = x
        if y is not None:
            self._position[1] = y

    def set_position_relative(self, dx, dy):
        if dx is not None:
            self.set_position(self._position[0] + dx, None)
        if dy is not None:
            self.set_position(None, self._position[1] + dy)
