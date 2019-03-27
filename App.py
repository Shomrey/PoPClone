import pygame


class App:
    def __init__(self):
        self._screen = None
        self._clock = None
        self._done = False
        self._position = [30, 30]

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode((400, 300))
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
        if pressed[pygame.K_UP]: self._position[1] -= 3
        if pressed[pygame.K_DOWN]: self._position[1] += 3
        if pressed[pygame.K_LEFT]: self._position[0] -= 3
        if pressed[pygame.K_RIGHT]: self._position[0] += 3

    def on_render(self):
        self._screen.fill((0, 0, 0))
        pygame.draw.rect(self._screen, (0, 128, 255), pygame.Rect(self._position[0], self._position[1], 60, 60))
        pygame.display.flip()   # this call is required to perform updates to the game screen

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._done = True

    def on_cleanup(self):
        pass
