import pygame
from math import fabs
import scene.SceneBase as SB

width = 50
height = 70
attackWidth = 30
FPS = 60
attackTime = 2*FPS
attackRange = 25

attackRight = [pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_1.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_2.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_3.png'), (width+attackWidth,height)),
               pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_4.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_5.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_6.png'), (width+attackWidth,height)),
               pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_7.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_8.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Attack_9.png'), (width+attackWidth,height))]

attackLeft = [pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_1.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_2.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_3.png'), (width+attackWidth,height)),
               pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_4.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_5.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_6.png'), (width+attackWidth,height)),
               pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_7.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_8.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_9.png'), (width+attackWidth,height))]


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, position, screen_number):
        pygame.sprite.Sprite.__init__(self)
        self._player = player
        self._position = position
        self._sprite_size = [width, height]
        self._image = pygame.transform.scale(pygame.image.load('png/EnemyAttack/Left_Attack_1.png'), self._sprite_size)
        self._distance_to_player = 1000
        self._direction = "Left"
        self._walkCount = 0
        self._perform_attack_range = 200
        self._attack_time = 0
        self._is_alive = True
        self._screen_number = screen_number

    def insta_kill(self):
        self._is_alive = False

    def get_screen_number(self):
        return self._screen_number

    def get_distance_to_player(self):
        player_position = self._player.get_position()
        #needs to be more precise
        return fabs(self._position[0] - (player_position[0] + width//2))

    def set_stationary_image(self):
        if self._direction == "Right":
            self._image = attackRight[0]
        else:
            self._image = attackLeft[0]

    def on_update(self):
        player_position = self._player.get_position()
        self._direction = "Left" if self._position[0] > player_position[0] else "Right"
        distance = self.get_distance_to_player()
        if self._position[0] < self._player.get_edge() < self._position[0] + width and self._position[1] - height <= self._player.get_position()[1] <= self._position[1] :
            self._is_alive = False
        if distance < self._perform_attack_range:
            self._attack_time += 1
            if self._attack_time > attackTime:
                self._image = attackLeft[self._walkCount//4]
                self._walkCount += 1
                if self._walkCount == 27:
                    if distance < attackRange:
                        self._player.change_health(-1)
                if self._walkCount >= 36:
                    self._walkCount = 0
                    self._attack_time = 0
                    self.set_stationary_image()
        else:
            self.set_stationary_image()
            self._image = attackLeft[0]
            self._walkCount = 0
            self._attack_time = 0

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

    def is_alive(self):
        return self._is_alive
