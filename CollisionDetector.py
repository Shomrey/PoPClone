import pygame
from enum import Enum


class Side(Enum):
    ALL = 0
    TOP = 1
    TOP_LEFT = 2
    TOP_RIGHT = 3
    MID = 4
    MID_LEFT = 5
    MID_RIGHT = 6
    BOT = 7
    BOT_LEFT = 8
    BOT_RIGHT = 9


class CollisionDetector:
    def __init__(self, player, scene_floors):
        self._player = player
        self._player_rect_all = pygame.Rect(0, 0, 0, 0)
        self._player_rect_top = pygame.Rect(0, 0, 0, 0)
        self._player_rect_top_left = pygame.Rect(0, 0, 0, 0)
        self._player_rect_top_right = pygame.Rect(0, 0, 0, 0)
        self._player_rect_mid = pygame.Rect(0, 0, 0, 0)
        self._player_rect_mid_left = pygame.Rect(0, 0, 0, 0)
        self._player_rect_mid_right = pygame.Rect(0, 0, 0, 0)
        self._player_rect_bot = pygame.Rect(0, 0, 0, 0)
        self._scene_floors = scene_floors

    def on_update(self):
        self._player_rect_all = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1], 50, 70)
        self._player_rect_top = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1], 50, 20)
        self._player_rect_top_left = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1], 20, 20)
        self._player_rect_top_right = pygame.Rect(self._player.get_position()[0]+30, self._player.get_position()[1], 20, 20)
        self._player_rect_mid = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1] + 20, 50, 30)
        self._player_rect_mid_left = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1] + 20, 20, 30)
        self._player_rect_mid_right = pygame.Rect(self._player.get_position()[0]+30, self._player.get_position()[1] + 20, 20, 30)
        self._player_rect_bot = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1] + 50, 50, 20)

    def check_collision(self, side):
        if side == Side.ALL:
            return self._player_rect_all.collidelist(self._scene_floors) >= 0
        elif side == Side.TOP:
            return self._player_rect_top.collidelist(self._scene_floors) >= 0
        elif side == Side.TOP_LEFT:
            return self._player_rect_top_left.collidelist(self._scene_floors) >= 0
        elif side == Side.TOP_RIGHT:
            return self._player_rect_top_right.collidelist(self._scene_floors) >= 0
        elif side == Side.MID:
            return self._player_rect_mid.collidelist(self._scene_floors) >= 0
        elif side == Side.MID_LEFT:
            return self._player_rect_mid_left.collidelist(self._scene_floors) >= 0
        elif side == Side.MID_RIGHT:
            return self._player_rect_mid_right.collidelist(self._scene_floors) >= 0
        elif side == Side.BOT:
            return self._player_rect_bot.collidelist(self._scene_floors) >= 0
        else:
            raise NotImplementedError

    def check_on_edge(self, side):
        if side == Side.TOP:
            return self._player_rect_top_left.collidelist(self._scene_floors) != self._player_rect_top_right.collidelist(self._scene_floors)
        elif side == Side.MID:
            return self._player_rect_mid_left.collidelist(self._scene_floors) != self._player_rect_mid_right.collidelist(self._scene_floors)
        else:
            raise NotImplementedError

    def check_can_climb(self):
        rect1 = pygame.Rect(self._player.get_position()[0], self._player.get_position()[1]-30, 50, 10)
        return rect1.collidelist(self._scene_floors) < 0

    def update_floors(self, scene_floors):
        self._scene_floors = scene_floors
