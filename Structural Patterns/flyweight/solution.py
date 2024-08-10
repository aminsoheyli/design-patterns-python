'''
    With this implementation we're storing all icon of a IconType in a single place in memory
    So with the flyweight pattern:
            We need to separate the data that we need to share store it somewhere else in a flyweight class(PointIcon)
            and then implement a factory for caching these objects
'''
from enum import Enum


class PointType(Enum):
    HOSPITAL = 0
    CAFE = 1
    RESTAURANT = 2

    def __str__(self):
        return self.name


class PointIcon:
    def __init__(self, point_type, icon):
        self._type = point_type
        self._icon = icon

    @property
    def type(self):
        return self._type

    @property
    def icon(self):
        return self._icon


class PointIconFactory:
    def __init__(self):
        self.icons = {}

    def get_point_icon(self, type: PointType) -> PointIcon:
        if type not in self.icons:
            self.icons[type] = PointIcon(type, None)
        return self.icons[type]


class Point:
    def __init__(self, x, y, icon: PointIcon):
        self.x = x
        self.y = y
        self.icon = icon

    def draw(self):
        print(f'{self.icon.type} at ({self.x},{self.y})')


class PointService:
    def __init__(self, icon_factory: PointIconFactory):
        self.icon_factory = icon_factory

    def get_points(self):
        points = [Point(1, 2, self.icon_factory.get_point_icon(PointType.CAFE))]
        return points


if __name__ == '__main__':
    service = PointService(PointIconFactory())
    for point in service.get_points():
        point.draw()
