from abc import ABC, abstractmethod
from ava_filters.filters import Caramel


class Image:
    pass


class Filter(ABC):
    @abstractmethod
    def apply(self, image):
        pass


class VividFilter(Filter):
    def apply(self, image):
        print('Applying Vivid Filter')


# Adapter using composition
class CaramelFilterAdapter(Filter):
    def __init__(self, caramel):
        self.caramel = caramel

    def apply(self, image):
        self.caramel.render(image)


# Adapter using inheritance
class CaramelAdapter(Caramel, Filter):
    def apply(self, image):
        self.init()
        self.render(image)


class ImageView:
    def __init__(self, image):
        self.image = image

    def apply(self, filter: Filter):
        filter.apply(self.image)


if __name__ == '__main__':
    image_view = ImageView(Image())
    image_view.apply(VividFilter())
    print('Adapter using composition:')
    image_view.apply(CaramelFilterAdapter(Caramel()))
    print('Adapter using inheritance:')
    image_view.apply(CaramelAdapter())
