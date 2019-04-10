import pygame

runRight = [pygame.transform.scale(pygame.image.load('png/Run/Right_1.png'), (50,70)), pygame.transform.scale(pygame.image.load('png/Run/Right_2.png'), (50,70)), pygame.transform.scale(pygame.image.load('png/Run/Right_3.png'), (50,70)),
            pygame.transform.scale(pygame.image.load('png/Run/Right_4.png'), (50,70)), pygame.transform.scale(pygame.image.load('png/Run/Right_5.png'), (50,70)), pygame.transform.scale(pygame.image.load('png/Run/Right_6.png'), (50,70)),
            pygame.transform.scale(pygame.image.load('png/Run/Right_7.png'), (50,70)), pygame.transform.scale(pygame.image.load('png/Run/Right_8.png'), (50,70)), pygame.transform.scale(pygame.image.load('png/Run/Right_9.png'), (50,70))]



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._position = [20, 210]
        self._sprite_size = [50, 70]
        self._image = pygame.transform.scale(pygame.image.load("player.jpg"), self._sprite_size)
        self._direction = "Right"
        self._walkCount = 0

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

    def right_movement_animation(self):
        self._direction = "Right"
        self._image = runRight[self._walkCount]
        print(self._walkCount)
        self._walkCount += 1
        if self._walkCount >= 9:
            self._walkCount = 0

