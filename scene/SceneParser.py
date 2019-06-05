from xml.dom import minidom
from collections import defaultdict
from scene.SceneLayer import SceneLayer
from scene.render.Rectangle import Rectangle
from scene.render.Image import Image
from parse import parse
import os


LAYERS_NAMES = {SceneLayer.BACKGROUND:      "LEVEL_BACKGROUND",
                SceneLayer.FOREGROUND:      "LEVEL_FOREGROUND",
                SceneLayer.PHYSICAL_SCENE:  "LEVEL_FLOORS",
                SceneLayer.SCREEN_BORDERS:  "SCREEN_BORDERS"}

class SceneParser:
    @staticmethod
    def parse(scene_file_path):
        """
        Parse all elements of the scene in the given file.

        Each layer is a list of Renderable objects. The objects' dimensions are absolute pixels values
        characterizing the original image. They have to be converted to proper on-screen values.
        Each scene consists of multiple screenshots-part of the scene between two screen borders.
        Ergo: one file-one scene-multiple screenshots.
        :param scene_file_path: path to the scene to parse
        :return: a dictionary of geometry layers and scene resolution in pixels
        """
        geometry = defaultdict(lambda: [])

        xml_file = minidom.parse(os.path.abspath(scene_file_path))

        root = xml_file.getElementsByTagName('svg')[0]
        scene_width = float(root.attributes['width'].value)
        scene_height = float(root.attributes['height'].value)
        scene_resolution = (scene_width, scene_height)

        layers = xml_file.getElementsByTagName('g')  # 'g' is the tag name for a layer

        # Parse game elements from sublayers of GAME_ELEMENTS layer
        game_elements = next((layer.getElementsByTagName('g') for layer in layers if layer.attributes['inkscape:label'].value == "GAME_ELEMENTS"), [])
        geometry[SceneLayer.START_POSITION] = SceneParser._parse_layer(game_elements, "START_POSITION", scene_resolution)

        # Parse the rest of the layers
        for layer, layer_name in LAYERS_NAMES.items():
            geometry[layer] = SceneParser._parse_layer(layers, layer_name, scene_resolution)

        return geometry, scene_resolution

    @staticmethod
    def _parse_layer(layers, layer_name, scene_resolution):
        layer = next((layer for layer in layers
                      if layer.attributes['inkscape:label'].value == layer_name), None)

        if layer is not None:
            rectangle_xmls = layer.getElementsByTagName('rect')
            rectangles = [SceneParser._parse_rect_from_xml(rect, scene_resolution) for rect in rectangle_xmls]

            image_xmls = layer.getElementsByTagName('image')
            images = [SceneParser._parse_image_from_xml(image, scene_resolution) for image in image_xmls]

            return rectangles + images
        else:
            return []

    @staticmethod
    def _parse_dimensions_from_xml(xml_element, scene_resolution):
        x = float(SceneParser._parse_value(xml_element.attributes['x'].value, 'x', scene_resolution))
        y = float(SceneParser._parse_value(xml_element.attributes['y'].value, 'y', scene_resolution))
        width = float(SceneParser._parse_value(xml_element.attributes['width'].value, 'x', scene_resolution))
        height = float(SceneParser._parse_value(xml_element.attributes['height'].value, 'y', scene_resolution))
        return x, y, width, height

    @staticmethod
    def _parse_transform(xml_element):
        try:
            result = parse("scale({},{})", xml_element.attributes['transform'].value)
            scale_x, scale_y = float(result[0]), float(result[1])
            return scale_x, scale_y
        except KeyError:
            return 1, 1

    @staticmethod
    def _parse_rect_from_xml(rect, scene_resolution):
        """Returns a Rectangle object parsed from XML data"""
        x, y, width, height = SceneParser._parse_dimensions_from_xml(rect, scene_resolution)
        color = rect.attributes['style'].value[6:12]
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        return Rectangle(x, y, width, height, (r, g, b))

    @staticmethod
    def _parse_image_from_xml(image, scene_resolution):
        """Returns an Image object parsed from XML data"""
        x, y, width, height = SceneParser._parse_dimensions_from_xml(image, scene_resolution)
        scale_x, scale_y = SceneParser._parse_transform(image)
        filename = os.path.join("res/scenes/elements", os.path.split(image.attributes['xlink:href'].value)[1])
        return Image(x, y, width, height, filename, scale_x=scale_x, scale_y=scale_y)

    @staticmethod
    def _parse_value(value_str, dim,  scene_resolution):
        if '%' in value_str:
            relative_value = float(value_str.replace("%", "")) / 100.0
            return relative_value * (scene_resolution[0] if dim == 'x' else scene_resolution[1])
        return float(value_str)
