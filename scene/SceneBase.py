from abc import ABC, abstractmethod
from scene.SceneParser import SceneParser
from scene.SceneLayer import SceneLayer
from scene.render.Renderable import Renderable
from scene.PlayerOutOfScreenObserver import PlayerLeftScreen


class SceneBase(ABC):
    def __init__(self, screen_resolution, scene_file_path):
        self._screen_resolution = screen_resolution

        # contains all parsed geometry as well as the physical scene
        self._geometry, self._scene_resolution = SceneParser.parse(scene_file_path)
        screenshot_width = self.get_layer(SceneLayer.SCREEN_BORDERS)[1].get_x() - self.get_layer(SceneLayer.SCREEN_BORDERS)[0].get_x()  # TODO: Handle uneven screenshots
        self._screenshot_resolution = (screenshot_width, self._scene_resolution[1])
        self.reset_scene()

        # contains all layers to be rendered on every on_render call
        self._rendered_layers = [SceneLayer.BACKGROUND, SceneLayer.FOREGROUND]

    def on_update(self):
        pass

    @abstractmethod
    def on_render(self, screen):
        """Renders all layers stored in _rendered_layers list on the screen"""
        # screenshot_number = self.get_screenshot_number(player_position.x)

        for layer in self._rendered_layers:
            for rect in self._geometry[layer]:
                rect.on_render(screen, self._screenshot_resolution, self._screenshot_resolution[0] * self._current_screenshot)

    def get_layer(self, layer):
        """
        Returns a list of rectangles representing one layer of the scene

        :param layer - SceneLayer enum class instance
        """
        return self._geometry[layer]

    def get_screenshot_number(self, x):
        return x // self._screenshot_resolution[0]

    def get_current_screenshot(self):
        return self._current_screenshot

    def get_screenshot_resolution(self):
        return self._screenshot_resolution

    def get_start_position(self, screen_rect):
        start_position_rect = Renderable.to_screen_rect(self.get_layer(SceneLayer.START_POSITION)[0].get_rect(), screen_rect, self._screenshot_resolution, self._screenshot_resolution[0] * self._current_screenshot)

        return [start_position_rect.x, start_position_rect.y]

    def get_enemies(self, screen_rect):
        enemies = self.get_layer(SceneLayer.ENEMIES)
        enemies_to_return = []
        for enemy in enemies:
            enemy_rect = enemy.get_rect()
            enemy_info = []
            enemy_info.append(enemy_rect.x)
            enemy_info.append(enemy_rect.y)
            enemy_info.append(SceneBase.get_screenshot_number(self, enemy.get_rect().x))
            enemies_to_return.append(enemy_info)

        return enemies_to_return

    def get_potions(self, screen_rect):
        potions = self.get_layer(SceneLayer.POTIONS)
        potions_to_return = []
        for potion in potions:
            potion_rect = potion.get_rect()
            potion_info = []
            potion_info.append(potion_rect.x)
            potion_info.append(potion_rect.y)
            potion_info.append(SceneBase.get_screenshot_number(self, potion.get_rect().x))
            potions_to_return.append(potion_info)
        return potions_to_return

    def get_traps(self, screen_rect):
        traps = self.get_layer(SceneLayer.TRAPS)
        traps_to_return = []
        for trap in traps:
            trap_rect = trap.get_rect()
            trap_info = []
            trap_info.append(trap_rect.x)
            trap_info.append(trap_rect.y)
            trap_info.append(SceneBase.get_screenshot_number(self, trap.get_rect().x))
            traps_to_return.append(trap_info)
        return traps_to_return

    def get_current_screenshot_floors(self, screen):
        floors = [Renderable.to_screen_rect(
            rect.get_rect(), screen.get_rect(), self.get_screenshot_resolution(),
            self.get_screenshot_resolution()[0] * self.get_current_screenshot())
            for rect in self.get_layer(SceneLayer.PHYSICAL_SCENE)]
        return floors

    def handle_screenshot_change(self, playerLeftScreen):
        if playerLeftScreen.type == PlayerLeftScreen.Type.LEFT_LEFT:
            self._current_screenshot -= 1
        elif playerLeftScreen.type == PlayerLeftScreen.Type.LEFT_RIGHT:
            self._current_screenshot += 1
        elif playerLeftScreen.type == PlayerLeftScreen.Type.LEFT_DOWN:
            self.reset_scene()
        if self._current_screenshot < 0 or self._current_screenshot >= (self._scene_resolution[0] // self._screenshot_resolution[0]):
            raise RuntimeError("Player left the screen where he should not.")

    def reset_scene(self):
        self._current_screenshot = self.get_screenshot_number(self.get_layer(SceneLayer.START_POSITION)[0].get_x())

    def handle_player_killed(self, playerKilled):
        self.reset_scene()

