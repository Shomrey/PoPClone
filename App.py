import pygame


class App:
    screen_size = [712, 560]
    
    def manage_collision(self):
        if(self._rect.colliderect(pygame.Rect(self._position, self._size))):
            if self._speed[1] < 0 :
                self._position[1] = self._rect[1] - self._size[1]
                self._midair = False
                self._speed[1] = 0
            elif self._speed[1] > 0 : 
                self._speed[1] *= -0.2
                self._position[1] += 10
        else:
            pass
    
    def __init__(self):
        self._screen = None
        self._clock = None
        self._done = False
        self._size = [60, 60]
        self._position = [30, App.screen_size[1] - self._size[1]]
        #physics variables
        self._speed = [3, 0]
        self._jump_speed = 15
        self._midair = False
        self._g = -0.4
        #temporary, object on a map
        self._rect = pygame.Rect(App.screen_size[0]*0.6, App.screen_size[1]*0.6, 150, 20)

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(App.screen_size)
        self._clock = pygame.time.Clock()

    def on_execute(self):
        if self.on_init() is False:
            self._done = True

        while not self._done:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_update()
            self.on_render()
            self._clock.tick(60) # slow down to 60 fps

        self.on_cleanup()

    def on_update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: self._speed[0] = -3
        elif pressed[pygame.K_RIGHT]: self._speed[0] = 3
        else: self._speed[0] = 0
        if pressed[pygame.K_DOWN]: self._midair = True
        
        #movement part
        self._position[0] += self._speed[0]
        
        if (not self._midair and (pressed[pygame.K_UP] or pressed[pygame.K_SPACE])) : 
            self._midair = True
            self._speed[1] += self._jump_speed
            
        if self._midair == True :
            self._position[1] -= self._speed[1]
            self._speed[1] += self._g
            
        if self._position[1] > App.screen_size[1] - 1.2*self._size[1] :
            self._position[1] = App.screen_size[1] - self._size[1]
            self._midair = False
            self._speed[1] = 0
            
        self.manage_collision()

    def on_render(self):
        self._screen.fill((0, 0, 0))
        pygame.draw.rect(self._screen, (0, 128, 255), pygame.Rect(self._position, self._size))
        pygame.draw.rect(self._screen, (60, 60, 60), self._rect)
        pygame.display.flip()   # this call is required to perform updates to the game screen

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._done = True

    def on_cleanup(self):
        pygame.quit()
