from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def clone(self) -> 'Component':
        pass


class Circle(Component):
    def __init__(self):
        self._radius = None

    def render(self):
        print('Rendering a circle')

    def clone(self) -> 'Component':
        new_circle = Circle()
        new_circle.radius = self._radius
        return new_circle

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value


class ContextMenu:
    def duplicate(self, component):
        new_component = component.clone()
        # Add target to our document
