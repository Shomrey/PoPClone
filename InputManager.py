import pygame


class InputManager:
    def __init__(self, player):
        self._player = player
        self._crouching = False

    def on_update(self):
        pressed = pygame.key.get_pressed()

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

    def _jump_up(self):
        self._player.set_position_relative(None, -3)

    def _jump_left(self):
        self._player.set_position_relative(None, -3)

    def _jump_right(self):
        self._player.set_position_relative(None, -3)

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
