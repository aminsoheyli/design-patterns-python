from abc import ABC, abstractmethod


class Compressor(ABC):
    @abstractmethod
    def compress(self, filename):
        pass


class Filter(ABC):
    @abstractmethod
    def apply(self, filename):
        pass


class ImageStorage:
    def store(self, filename, compressor: Compressor, filter: Filter):
        compressor.compress(filename)
        filter.apply(filename)
        print(f'Storing {filename}')


class JpegCompressor(Compressor):
    def compress(self, filename):
        print(f'Compressing {filename} using JPEG')


class PngCompressor(Compressor):
    def compress(self, filename):
        print(f'Compressing {filename} using PNG')


class BlackAndWhiteFilter(Filter):
    def apply(self, filename):
        print(f'Applying B&W filter on {filename}')


class HighContrastFilter(Filter):
    def apply(self, filename):
        print(f'Applying High Contrast filter on {filename}')


if __name__ == '__main__':
    imageStorage = ImageStorage()
    imageStorage.store('screenshot', JpegCompressor(), BlackAndWhiteFilter())
    imageStorage.store('screenshot', PngCompressor(), BlackAndWhiteFilter())
