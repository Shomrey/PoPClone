import pygame
import queue
from CollisionDetector import CollisionDetector, Side


class InputManager:
    def __init__(self, player, scene_floors):
        self._player = player
        self._scene_floors = scene_floors
        self._detector = CollisionDetector(player, scene_floors)
        self._jump_queue = queue.Queue()
        self._jump_x = 0
        self._crouching = False
        self._none_pressed = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def on_update(self):
        pressed = pygame.key.get_pressed()
        self._detector.on_update()

        if self._detector.check_collision(Side.TOP):
            while not self._jump_queue.empty(): self._jump_queue.get()
            jump_values = (-8, -7, -6)
            for i in jump_values: self._jump_queue.put(i)

        if self._detector.check_collision(Side.BOT):
            while not self._jump_queue.empty(): self._jump_queue.get()
        else:
            self._jump_queue.put(9)

        if not self._jump_queue.empty():
            pressed = self._none_pressed
            self._jump_continue()
        if self._player.get_health() > 0:
            if pressed[pygame.K_SPACE]:
                self._attack()
            else:
                if pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]: pass
                elif pressed[pygame.K_LEFT]: self._move_left()
                elif pressed[pygame.K_RIGHT]: self._move_right()

                if pressed[pygame.K_LEFT] and pressed[pygame.K_UP]: self._jump_left()
                elif pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]: self._jump_right()
                elif pressed[pygame.K_UP]: self._jump_up()

        if pressed[pygame.K_DOWN]:
            self._crouch()
        else:
            if self._crouching:
                self._stand_up()

    def update_floors(self, scene_floors):
        self._scene_floors = scene_floors
        self._detector.update_floors(scene_floors)

    def _jump_up(self):
        jump_values = (-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0)  # 45
        for i in jump_values: self._jump_queue.put(i)
        self._jump_x = 0
        self._jump_continue()

    def _jump_left(self):
        jump_values = (-9, -8, -6, -5, -3, -2, 0, 0, 0, 2, 3, 5, 6, 8, 9)  # 33
        for i in jump_values: self._jump_queue.put(i)
        self._jump_x = -6
        self._jump_continue()

    def _jump_right(self):
        jump_values = (-9, -8, -6, -5, -3, -2, 0, 0, 0, 2, 3, 5, 6, 8, 9)
        for i in jump_values: self._jump_queue.put(i)
        self._jump_x = 6
        self._jump_continue()

    def _jump_continue(self):
        self._player.set_position_relative(self._jump_x, self._jump_queue.get())

    def _move_left(self):
        self._player.set_position_relative(-3, None)
        self._player.left_movement_animation()

    def _move_right(self):
        self._player.set_position_relative(3, None)
        self._player.right_movement_animation()

    def _crouch(self):
        self._crouching = True

    def _stand_up(self):
        self._crouching = False

    def _attack(self):
        self._player.attack_animation()

