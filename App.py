import pygame
import os
from scene.BasicScene import BasicScene
from scene.SceneLayer import SceneLayer
from scene.render.Renderable import Renderable
from Player import Player
from InputManager import InputManager
from Enemy import Enemy
from scene.PlayerOutOfScreenObserver import PlayerOutOfScreenObserver, PlayerLeftScreen


class App:
    def __init__(self):
        self._screen = None
        self._clock = None
        self._done = False
        self._player = None
        self._input_manager = None
        self._resolution = (760, 520)
        self._enemies = []
        self._number_of_enemies = 0
        self._scene = BasicScene(self._resolution, os.path.join(os.getcwd(), 'res/scenes/presentation_level.svg'))
        self._player_observer = PlayerOutOfScreenObserver(self._resolution)
        self._player_observer.subscribe(PlayerLeftScreen, self._scene.handle_screenshot_change)

    def on_init(self):
        pygame.init()
        self._screen = pygame.display.set_mode(self._resolution)
        self._clock = pygame.time.Clock()
        starting_point = self._scene.get_start_position(self._screen.get_rect())
        self._player = Player(starting_point)
        enemies = self._scene.get_enemies(self._screen.get_rect())
        print("----")
        print(enemies)
        for enemy in enemies:
            print(enemy[0], enemy[1])
            enemy_to_spawn = [enemy[0], enemy[1]]
            print(enemy_to_spawn)
            self.spawn_enemy(self._player, enemy_to_spawn)
            print("I am spawned")
        print("enemies spawned")
        potions = self._scene.get_potions(self._screen.get_rect())
        traps = self._scene.get_traps(self._screen.get_rect())
        floors = [Renderable.to_screen_rect(rect.get_rect(), self._screen.get_rect(), self._scene.get_screenshot_resolution(), self._scene.get_screenshot_resolution()[0] * self._scene.get_current_screenshot())
                  for rect in self._scene.get_layer(SceneLayer.PHYSICAL_SCENE)]
        self._input_manager = InputManager(self._player, floors)
        for potion in potions:
            self.add_potion(self._player, potion)
        for trap in traps:
            self.create_trap(self._player, trap)
        print("------------------------")
        #self.add_potion(self._player, [300,308])
        #self.spawn_enemy(self._player, [500, 258])
        #self.add_potion(self._player, [550,308])
        #self.create_trap(self._player, [400, 308])

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
        self._input_manager.on_update()
        for i in range(self._number_of_enemies):
            if self._enemies[i].is_alive(): self._enemies[i].on_update()
        self._player_observer.check_player_position(self._player)

    def on_render(self):
        self._scene.on_render(self._screen)
        self._player.on_render(self._screen)
        for i in range(self._number_of_enemies):
            if self._enemies[i].is_alive(): self._enemies[i].on_render(self._screen)
        pygame.display.flip()   # this call is required to perform updates to the game screen


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._done = True

    def on_cleanup(self):
        pass

    def spawn_enemy(self, player, position):
        enemy = Enemy(player, position)
        self._enemies.append(enemy)
        self._number_of_enemies += 1

    def create_trap(self, player, position):
        player._traps.append(position)

    def add_potion(self, player, position):
        player._potions.append(position)
