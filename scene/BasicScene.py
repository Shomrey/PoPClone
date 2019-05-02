from scene.SceneBase import SceneBase


class BasicScene(SceneBase):
    def __init__(self, screen_resolution, scene_file_path):
        super(BasicScene, self).__init__(screen_resolution, scene_file_path)

    def on_render(self, screen):
        super(BasicScene, self).on_render(screen)
