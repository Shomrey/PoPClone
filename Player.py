import pygame

width = 50
height = 70
attackWidth = 30
frameSlow = 3

runRight = [pygame.transform.scale(pygame.image.load('png/Run/Right_1.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Right_2.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Right_3.png'), (width,height)),
            pygame.transform.scale(pygame.image.load('png/Run/Right_4.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Right_5.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Right_6.png'), (width,height)),
            pygame.transform.scale(pygame.image.load('png/Run/Right_7.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Right_8.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Right_9.png'), (width,height))]

runLeft = [pygame.transform.scale(pygame.image.load('png/Run/Left_1.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Left_2.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Left_3.png'), (width,height)),
           pygame.transform.scale(pygame.image.load('png/Run/Left_4.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Left_5.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Left_6.png'), (width,height)),
           pygame.transform.scale(pygame.image.load('png/Run/Left_7.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Left_8.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Run/Left_9.png'), (width,height))]

jump = [pygame.transform.scale(pygame.image.load('png/Jump/Jump_001.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Jump/Jump_002.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Jump/Jump_003.png'), (width,height)),
           pygame.transform.scale(pygame.image.load('png/Jump/Jump_004.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Jump/Jump_005.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Jump/Jump_006.png'), (width,height)),
           pygame.transform.scale(pygame.image.load('png/Jump/Jump_007.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Jump/Jump_008.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Jump/Jump_009.png'), (width,height))]

attackRight = [pygame.transform.scale(pygame.image.load('png/Attack/Attack__000.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Attack__001.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Attack__002.png'), (width+attackWidth,height)),
               pygame.transform.scale(pygame.image.load('png/Attack/Attack__003.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Attack__004.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Attack__005.png'), (width+attackWidth,height)),
               pygame.transform.scale(pygame.image.load('png/Attack/Attack__006.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Attack__007.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Attack__008.png'), (width+attackWidth,height))]

attackLeft = [pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__000.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__001.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__002.png'), (width+attackWidth,height)),
               pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__003.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__004.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__005.png'), (width+attackWidth,height)),
               pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__006.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__007.png'), (width+attackWidth,height)),pygame.transform.scale(pygame.image.load('png/Attack/Left_Attack__008.png'), (width+attackWidth,height))]

death = [pygame.transform.scale(pygame.image.load('png/Death/Dead__000.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Death/Dead__002.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Death/Dead__003.png'), (width,height)),
           pygame.transform.scale(pygame.image.load('png/Death/Dead__004.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Death/Dead__005.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Death/Dead__006.png'), (width,height)),
           pygame.transform.scale(pygame.image.load('png/Death/Dead__007.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Death/Dead__008.png'), (width,height)), pygame.transform.scale(pygame.image.load('png/Death/Dead__009.png'), (width,height))]


hearth = pygame.transform.scale(pygame.image.load('png/hearth.svg'), (15, 15))

potion = pygame.transform.scale(pygame.image.load('png/potion.png'), (20, 20))



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._position = [20, 258]
        self._sprite_size = [width, height]
        self._image = pygame.transform.scale(pygame.image.load('png/Run/Right_1.png'), self._sprite_size)
        self._direction = "Right"
        self._walkCount = 0
        self._inAir = False
        self._health = 3
        self._edge = 0
        self._potions = []
        self._traps = []


    def on_update(self):
        if self._health <= 0:
            #disable Input Manager
            self.death_animation()
        if len(self._potions) > 0:
            for i in self._potions:
                if i[0] < self._position[0]+width//2 < i[0] + 20 and i[1] >= self._position[1] >= i[1] - 20:
                    self._potions.remove(i)
                    self._health += 1
        if len(self._traps) > 0:
            for i in self._traps:
                if i[0] < self._position[0]+width//2 < i[0] + 20 and i[1] == self._position[1]:
                    self._health = 0

    def on_render(self, screen):
        position_rect = self._image.get_rect().move(self._position[0], self._position[1])
        screen.blit(self._image, position_rect)
        for i in range(self._health):
            screen.blit(hearth, [10 + 15*i, 20])
        for i in range(len(self._potions)):
            screen.blit(potion, self._potions[i])

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
        self._edge = 0
        self._image = runRight[self._walkCount//frameSlow]
        self._walkCount += 1
        if self._walkCount >= 9*frameSlow:
            self._walkCount = 0

    def left_movement_animation(self):
        self._direction = "Left"
        self._edge = 0
        self._image = runLeft[self._walkCount//frameSlow]
        self._walkCount += 1
        if self._walkCount >= 9*frameSlow:
            self._walkCount = 0

    def jump_animation(self):
        self._direction = "Up"
        self._inAir = True
        self._image = jump[self._walkCount//frameSlow]
        self._walkCount += 1
        if self._walkCount >= 9*frameSlow:
            self._walkCount = 0

    def attack_animation(self):
        if self._walkCount >=9:
            self._walkCount = self._walkCount//frameSlow
        FPS, timer = 60, 0
        if self._direction == "Right":
            timer = 1 * FPS
            while timer != 0:
                timer -= 1
            self._image = attackRight[self._walkCount]
            if self._walkCount >= 3:
                self._edge = width + attackWidth + self._position[0]
            self._walkCount += 1
            if self._walkCount >= 9:
                self._walkCount = 0
        elif self._direction == "Left":
            timer = 1 * FPS
            while timer != 0:
                timer -= 1
            self._image = attackLeft[self._walkCount]
            if self._walkCount >= 3:
                self._edge = self._position[0] - attackWidth
            self._walkCount += 1
            if self._walkCount >= 9:
                self._walkCount = 0

    def change_health(self, value):
        self._health += value

    def death_animation(self):
        FPS, timer = 60, 0
        for i in range(9):
            timer = 1 * FPS
            while timer != 0:
                timer -= 1
            self._image = death[i]
            self._walkCount += 1

    def get_health(self):
        return self._health

    def get_edge(self):
        return self._edge