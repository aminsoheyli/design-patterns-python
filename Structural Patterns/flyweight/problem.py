from enum import Enum


class PointType(Enum):
    HOSPITAL = 0
    CAFE = 1
    RESTAURANT = 2

    def __str__(self):
        return self.name


class Point:
    def __init__(self, x, y, point_type: PointType, icon: []):
        self.x = x
        self.y = y
        self.type = point_type
        self.icon = icon

    def draw(self):
        print(f'{self.type} at ({self.x},{self.y})')


class PointService:
    @staticmethod
    def get_points():
        points = [Point(1, 2, PointType.CAFE, None)]
        return points


if __name__ == '__main__':
    service = PointService()
    for point in service.get_points():
        point.draw()
