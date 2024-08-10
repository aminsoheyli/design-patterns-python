from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Shape(Component):
    def render(self):
        print('Render Shape')

    def move(self):
        print('Move Shape')


class Group(Component):
    def __init__(self):
        self.components = []

    def add(self, component: Component):
        self.components.append(component)

    def render(self):
        for component in self.components:
            component.render()

    def move(self):
        for component in self.components:
            component.move()


if __name__ == '__main__':
    group1 = Group()
    group1.add(Shape())  # square
    group1.add(Shape())  # square

    group2 = Group()
    group2.add(Shape())  # circle
    group2.add(Shape())  # circle

    group = Group()
    group.add(group1)
    group.add(group2)

    group.render()
    group.move()
