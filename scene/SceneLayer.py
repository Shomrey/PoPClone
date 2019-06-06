from enum import Enum


class SceneLayer(Enum):
    PHYSICAL_SCENE = 1
    BACKGROUND = 2
    FOREGROUND = 3
    SCREEN_BORDERS = 4
    START_POSITION = 5
    ENEMIES = 6
    TRAPS = 7
    POTIONS = 8
