from xml.dom import minidom
from collections import defaultdict
from scene.SceneLayer import SceneLayer
from scene.render.Rectangle import Rectangle
import pygame
import os


class SceneParser:
    @staticmethod
    def parse(scene_file_path, resolution):
        geometry = defaultdict(lambda: [])

        xml_file = minidom.parse(os.path.abspath(scene_file_path))

        root = xml_file.getElementsByTagName('svg')[0]
        screen_width = float(root.attributes['width'].value)
        screen_height = float(root.attributes['height'].value)
        scene_resolution = (screen_width, screen_height)

        layers = xml_file.getElementsByTagName('g')  # 'g' is the tag name for all layers

        # Background parsing
        geometry[SceneLayer.BACKGROUND] = SceneParser._parse_layer(layers, "LEVEL_BACKGROUND", resolution, scene_resolution)

        # Physical scene parsing
        geometry[SceneLayer.PHYSICAL_SCENE] = SceneParser._parse_layer(layers, "LEVEL_FLOORS", resolution, scene_resolution)

        return geometry

    @staticmethod
    def _parse_layer(layers, layer_name, resolution, scene_resolution):
        rectangles = next((layer.getElementsByTagName('rect') for layer in layers
                           if layer.attributes['inkscape:label'].value == layer_name), [])

        return [SceneParser._parse_rect_from_xml(rect, resolution, scene_resolution) for rect in rectangles]


    @staticmethod
    def _parse_rect_from_xml(rect, resolution, scene_resolution):
        """Returns a Rectangle object parsed from XML data"""
        x = float(SceneParser._value_parse(rect.attributes['x'].value, 'x', resolution, scene_resolution))
        y = float(SceneParser._value_parse(rect.attributes['y'].value, 'y', resolution, scene_resolution))
        width = float(SceneParser._value_parse(rect.attributes['width'].value, 'x', resolution, scene_resolution))
        height = float(SceneParser._value_parse(rect.attributes['height'].value, 'y', resolution, scene_resolution))
        color = rect.attributes['style'].value[6:12]
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        return Rectangle(x, y, width, height, (r, g, b))

    @staticmethod
    def _value_parse(value_str, dim, resolution, scene_resolution):
        if '%' in value_str:
            relative_value = float(value_str.replace("%", "")) / 100.0
            return relative_value * (resolution[0] if dim == 'x' else resolution[1])
        return float(value_str) / (scene_resolution[0] / resolution[0]
                                   if dim == 'x' else
                                   scene_resolution[1] / resolution[1])
