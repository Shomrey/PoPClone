import pygame
from scene.GameScene import GameScene
from Player import Player


class App:
    def __init__(self):
        self._screen = None
        self._clock = None
        self._done = False
        self._player = None
        self._resolution = (760, 520)
        self._scene = GameScene(self._resolution)

    def on_init(self):
        self._player = Player()
        pygame.init()
        self._screen = pygame.display.set_mode(self._resolution)
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
        self._scene.on_update()
        self._player.on_update()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self._player.set_position_relative(None, -3)
        if pressed[pygame.K_DOWN]: self._player.set_position_relative(None, 3)
        if pressed[pygame.K_LEFT]: self._player.set_position_relative(-3, None)
        if pressed[pygame.K_RIGHT]: self._player.set_position_relative(3, None)

    def on_render(self):
        self._scene.on_render(self._screen)
        self._player.on_render(self._screen)
        pygame.display.flip()   # this call is required to perform updates to the game screen

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._done = True

    def on_cleanup(self):
        pass