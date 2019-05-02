from scene.SceneBase import SceneBase, SceneLayer
from xml.dom import minidom
import os
import pygame


class TestScene(SceneBase):
    def __init__(self, resolution):
        SceneBase.__init__(self, resolution)
        self._floors = []
        self._background = []
        self._scene_resolution = (0, 0)
        self.build_geometry()

    def build_geometry(self):
        filepath = 'res/scenes/test_scene.svg'
        full_path = os.path.join(os.getcwd(), filepath)
        xml_file = minidom.parse(os.path.abspath(full_path))

        root = xml_file.getElementsByTagName('svg')[0]
        screen_width = float(root.attributes['width'].value)
        screen_height = float(root.attributes['height'].value)
        self._scene_resolution = (screen_width, screen_height)

        layers = xml_file.getElementsByTagName('g') # 'g' is the tag name for all layers

        background = next((layer.getElementsByTagName('rect') for layer in layers
                     if layer.attributes['inkscape:label'].value == "LEVEL_BACKGROUND"), [])

        for rect in background:
            self._background.append(self._parse_rect_from_xml(rect))

        floors = next((layer.getElementsByTagName('rect') for layer in layers
                     if layer.attributes['inkscape:label'].value == "LEVEL_FLOORS"), [])

        self._floors = [self._parse_rect_from_xml(rect) for rect in floors]
        self._geometry[SceneLayer.PHYSICAL_SCENE] = self._floors

    def on_render(self, screen):
        for rect in self._background:
            pygame.draw.rect(screen, rect[1], rect[0])

        for rect in self._floors:
            pygame.draw.rect(screen, rect[1], rect[0])

    def _parse_rect_from_xml(self, rect):
        x = float(self._value_parse(rect.attributes['x'].value, 'x'))
        y = float(self._value_parse(rect.attributes['y'].value, 'y'))
        width = float(self._value_parse(rect.attributes['width'].value, 'x'))
        height = float(self._value_parse(rect.attributes['height'].value, 'y'))
        color = rect.attributes['style'].value[6:12]
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        return pygame.Rect(x, y, width, height), (r, g, b)

    def _value_parse(self, value_str, dim):
        if '%' in value_str:
            relative_value = float(value_str.replace("%", "")) / 100.0
            return relative_value * (self._resolution[0] if dim == 'x' else self._resolution[1])
        return float(value_str) / (self._scene_resolution[0] / self._resolution[0]
                                   if dim == 'x' else
                                   self._scene_resolution[1] / self._resolution[0])
        # return float(value_str)

    def _to_screen_rect(self, rect):
        """Transforms relative-sized rect to screen sized rect"""
        return pygame.Rect(rect.x * self._resolution[0],
                           rect.y * self._resolution[1],
                           rect.width * self._resolution[0],
                           rect.height * self._resolution[1])
