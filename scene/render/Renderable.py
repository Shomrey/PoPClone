from abc import ABC, abstractmethod


class Renderable(ABC):
    @abstractmethod
    def on_render(self, screen):
        pass
