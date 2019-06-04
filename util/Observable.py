from abc import ABC, abstractmethod


class Event(ABC):
    pass


class Observable(ABC):
    @abstractmethod
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def event(self, event):
        for callback in self.subscribers:
            callback(event)
