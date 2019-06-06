from util.Observable import Event, Observable
from enum import Enum


class PlayerLeftScreen(Event):
    class Type(Enum):
        LEFT_RIGHT = 0
        LEFT_LEFT = 1
        LEFT_UP = 2
        LEFT_DOWN = 3

    def __init__(self, type, player):
        self.type = type
        self.player = player


class PlayerOutOfScreenObserver(Observable):
    def __init__(self, screen_resolution):
        super(PlayerOutOfScreenObserver, self).__init__()
        self.screen_resolution = screen_resolution

    def raise_event(self, type, player):
        # super(PlayerOutOfScreenObserver, self).event(PlayerLeftScreen(type=type, player=player))
        self.event(PlayerLeftScreen(type=type, player=player))

    def check_player_position(self, player):
        x = player.get_position()[0]
        y = player.get_position()[1]

        if x < 0:
            self.raise_event(PlayerLeftScreen.Type.LEFT_LEFT, player)
            player.set_position(x  + self.screen_resolution[0], y)
        elif x > self.screen_resolution[0]:
            self.raise_event(PlayerLeftScreen.Type.LEFT_RIGHT, player)
            player.set_position(x  - self.screen_resolution[0], y)
        elif y < 0:
            self.raise_event(PlayerLeftScreen.Type.LEFT_UP, player)
            # player.set_position(x, y + self.screen_resolution[0])
        elif y > self.screen_resolution[1]:
            self.raise_event(PlayerLeftScreen.Type.LEFT_DOWN, player)
            # player.set_position(x, y - self.screen_resolution[0])
