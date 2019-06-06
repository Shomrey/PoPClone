import pygame
import queue


class InputManager:
    def __init__(self, player, scene, screen):
        self._player = player
        self._player_rect_top = 0
        self._player_rect_bot = 0
        self._scene_resolution = (760, 520)
        self._scene = scene
        self._screen = screen
        self._jump_queue = queue.Queue()
        self._jump_x = 0
        self._crouching = False
        self._none_pressed = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def on_update(self):

        pressed = pygame.key.get_pressed()

        self._player_rect_top = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1], 50, 20)
        self._player_rect_bot = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1] + 50, 50, 20)

        scene_floors = self._scene.get_current_screenshot_floors(self._screen)

        if self._player_rect_top.collidelist(scene_floors) >= 0:
            while not self._jump_queue.empty(): self._jump_queue.get()
            jump_values = (-8, -7, -6)
            for i in jump_values: self._jump_queue.put(i)
            self._jump_queue.put(-9)

        if self._player_rect_bot.collidelist(scene_floors) < 0:
            self._jump_queue.put(9)
        else:
            while not self._jump_queue.empty(): self._jump_queue.get()

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



        if self._player.get_position()[0] < 0:
            self._player.set_position(0, None)
            self._jump_x = 0

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

