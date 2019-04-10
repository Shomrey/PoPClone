from scene.SceneBase import SceneBase
from xml.dom import minidom
import os
import pygame


class TestScene(SceneBase):
    def __init__(self, resolution):
        SceneBase.__init__(self, resolution)
        self._floors = []
        self._background = []
        self.build_geometry()

    def build_geometry(self):
        filepath = 'res/scenes/test_scene.svg'
        full_path = os.path.join(os.getcwd(), filepath)
        xml_file = minidom.parse(os.path.abspath(full_path))

        root = xml_file.getElementsByTagName('svg')[0]
        screen_width = float(root.attributes['width'].value)
        screen_height = float(root.attributes['height'].value)

        layers = xml_file.getElementsByTagName('g') # 'g' is the tag name for all layers

        background = next((layer.getElementsByTagName('rect') for layer in layers
                     if layer.attributes['inkscape:label'].value == "LEVEL_BACKGROUND"), [])

        for rect in background:
            self._background.append(TestScene._parse_rect_from_xml(rect))

        floors = next((layer.getElementsByTagName('rect') for layer in layers
                     if layer.attributes['inkscape:label'].value == "LEVEL_FLOORS"), [])

        floors = []
        for layer in layers:
            if layer.attributes['inkscape:label'].value == "LEVEL_FLOORS":
                floors = layer.getElementsByTagName('rect')

        self._floors = [TestScene._parse_rect_from_xml(rect) for rect in floors]

    def on_render(self, screen):
        for rect in self._background:
            pygame.draw.rect(screen, rect[1], rect[0])

        for rect in self._floors:
            pygame.draw.rect(screen, rect[1], rect[0])

    @staticmethod
    def _parse_rect_from_xml(rect):
        x = float(rect.attributes['x'].value)
        y = float(rect.attributes['y'].value)
        width = float(rect.attributes['width'].value)
        height = float(rect.attributes['height'].value)
        color = rect.attributes['style'].value[6:12]
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        return (pygame.Rect(x, y, width, height), (r, g, b))



