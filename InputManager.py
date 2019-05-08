import pygame


class InputManager:
    def __init__(self, player):
        self._player = player
        self._key_bindings = {
            pygame.K_UP:    self._jump,
            pygame.K_DOWN:  self._crouch,
            pygame.K_LEFT:  self._move_left,
            pygame.K_RIGHT: self._move_right,
            pygame.K_SPACE: self._attack
        }

    def on_update(self):
        if self._player.get_health() > 0:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:    self._key_bindings[pygame.K_UP]()
            if pressed[pygame.K_DOWN]:  self._key_bindings[pygame.K_DOWN]()
            if pressed[pygame.K_LEFT]:  self._key_bindings[pygame.K_LEFT]()
            if pressed[pygame.K_RIGHT]: self._key_bindings[pygame.K_RIGHT]()
            if pressed[pygame.K_SPACE]: self._key_bindings[pygame.K_SPACE]()

    def _jump(self):
        self._player.set_position_relative(None, -3)
        self._player.jump_animation()

    def _move_left(self):
        self._player.set_position_relative(-3, None)
        self._player.left_movement_animation()

    def _move_right(self):
        self._player.set_position_relative(3, None)
        self._player.right_movement_animation()

    def _crouch(self):
        self._player.set_position_relative(None, 3)

    def _attack(self):
        self._player.attack_animation()