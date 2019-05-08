from xml.dom import minidom
from collections import defaultdict
from scene.SceneLayer import SceneLayer
from scene.render.Rectangle import Rectangle
from scene.render.Image import Image
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

        # Parse all layers
        for layer, layer_name in dict([(SceneLayer.BACKGROUND, "LEVEL_BACKGROUND"),
                                            (SceneLayer.FOREGROUND, "LEVEL_FOREGROUND"),
                                            (SceneLayer.PHYSICAL_SCENE, "LEVEL_FLOORS"),
                                            (SceneLayer.SCREEN_BORDERS, "SCREEN_BORDERS")]).items():
            geometry[layer] = SceneParser._parse_layer(layers, layer_name, resolution, scene_resolution)

        return geometry

    @staticmethod
    def _parse_layer(layers, layer_name, resolution, scene_resolution):
        rectangle_xmls = next((layer.getElementsByTagName('rect') for layer in layers
                           if layer.attributes['inkscape:label'].value == layer_name), [])

        rectangles = [SceneParser._parse_rect_from_xml(rect, resolution, scene_resolution) for rect in rectangle_xmls]

        image_xmls = next((layer.getElementsByTagName('image') for layer in layers
                           if layer.attributes['inkscape:label'].value == layer_name), [])

        images = [SceneParser._parse_image_from_xml(image, resolution, scene_resolution) for image in image_xmls]

        return rectangles + images

    @staticmethod
    def _parse_dimensions_from_xml(xml_element, resolution, scene_resolution):
        x = float(SceneParser._parse_value(xml_element.attributes['x'].value, 'x', resolution, scene_resolution))
        y = float(SceneParser._parse_value(xml_element.attributes['y'].value, 'y', resolution, scene_resolution))
        width = float(SceneParser._parse_value(xml_element.attributes['width'].value, 'x', resolution, scene_resolution))
        height = float(SceneParser._parse_value(xml_element.attributes['height'].value, 'y', resolution, scene_resolution))
        return x, y, width, height

    @staticmethod
    def _parse_rect_from_xml(rect, resolution, scene_resolution):
        """Returns a Rectangle object parsed from XML data"""
        x, y, width, height = SceneParser._parse_dimensions_from_xml(rect, resolution, scene_resolution)
        color = rect.attributes['style'].value[6:12]
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        return Rectangle(x, y, width, height, (r, g, b))

    @staticmethod
    def _parse_image_from_xml(image, resolution, scene_resolution):
        """Returns an Image object parsed from XML data"""
        x, y, width, height = SceneParser._parse_dimensions_from_xml(image, resolution, scene_resolution)
        filename = os.path.join("res/scenes/elements", os.path.split(image.attributes['xlink:href'].value)[1])
        return Image(x, y, width, height, filename)

    @staticmethod
    def _parse_value(value_str, dim, resolution, scene_resolution):
        if '%' in value_str:
            relative_value = float(value_str.replace("%", "")) / 100.0
            return relative_value * (resolution[0] if dim == 'x' else resolution[1])
        return float(value_str) / (scene_resolution[0] / resolution[0]
                                   if dim == 'x' else
                                   scene_resolution[1] / resolution[1])
