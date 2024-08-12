from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self):
        pass


class Circle(Component):
    def __init__(self):
        self._radius = None

    def render(self):
        print('Rendering a circle')

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value


class ContextMenu:
    def duplicate(self, component):
        if component is Circle:
            target = Circle()
            target.radius = component.radius
            # Add target to our document
