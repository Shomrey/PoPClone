from abc import ABC, abstractmethod
from collections import defaultdict


class Event(ABC):
    pass


class Observable(ABC):
    @abstractmethod
    def __init__(self):
        self.subscribers = defaultdict(lambda: [])

    def subscribe(self, event_type, callback):
        """
        Subscribe to given event

        Params
        -------
        event_type - class (inheriting from Event abstract class) to subscribe to
        callback - callback to perform on the event class instance
        """
        self.subscribers[event_type.__name__].append(callback)

    def event(self, event):
        for callback in self.subscribers[event.__class__.__name__]:
            callback(event)
