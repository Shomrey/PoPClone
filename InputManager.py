import pygame
import queue


class InputManager:
    def __init__(self, player):
        self._player = player
        self._jump_queue = queue.Queue()
        self._jump_x = 0
        self._crouching = False
        self._none_pressed = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def on_update(self):
        pressed = pygame.key.get_pressed()

        if not self._jump_queue.empty():
            pressed = self._none_pressed
            self._jump_continue()

        if pressed[pygame.K_LEFT] and pressed[pygame.K_RIGHT]: pass
        elif pressed[pygame.K_LEFT]: self._move_left()
        elif pressed[pygame.K_RIGHT]: self._move_right()

        if pressed[pygame.K_LEFT] and pressed[pygame.K_UP]: self._jump_left()
        elif pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]: self._jump_right()
        elif pressed[pygame.K_UP]: self._jump_up()

        if self._crouching:
            if pressed[pygame.K_DOWN]: self._crouch()
            else: self._stand_up()

    def _jump_up(self):
        jump_values = (-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0)
        for i in jump_values: self._jump_queue.put(i)
        self._jump_x = 0
        self._jump_continue()

    def _jump_left(self):
        jump_values = (-9, -8, -6, -5, -3, -2, 0, 0, 0, 2, 3, 5, 6, 8, 9, 0, 0)
        for i in jump_values: self._jump_queue.put(i)
        self._jump_x = -6
        self._jump_continue()

    def _jump_right(self):
        jump_values = (-9, -8, -6, -5, -3, -2, 0, 0, 0, 2, 3, 5, 6, 8, 9, 0, 0)
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
        self._player.set_position_relative(None, 3)

    def _stand_up(self):
        self._crouching = False
