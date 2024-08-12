from abc import ABC, abstractmethod


class EBook(ABC):

    @abstractmethod
    def show(self):
        pass

    @property
    def file_name(self):
        pass


# Lazy initialization/loading
class EBookProxy(EBook):
    def __init__(self, file_name):
        self._file_name = file_name
        self._ebook = None

    def show(self):
        if self._ebook is None:
            self._ebook = RealEBook(self._file_name)
        self._ebook.show()

    @property
    def file_name(self):
        return self._file_name


class RealEBook(EBook):
    def __init__(self, file_name):
        self._file_name = file_name
        self.__load()

    def __load(self):
        print(f"Loading the ebook {self._file_name}")

    def show(self):
        print(f"Showing the ebook {self._file_name}")

    @property
    def file_name(self):
        return self._file_name


class LoggingEBookProxy(EBook):
    def __init__(self, file_name):
        self._file_name = file_name
        self._ebook = None

    def show(self):
        if self._ebook is None:
            self._ebook = RealEBook(self._file_name)
        print('Logging')
        self._ebook.show()

    @property
    def file_name(self):
        return self._file_name


class Library:
    def __init__(self):
        self._ebooks = {}

    def add(self, ebook):
        self._ebooks[ebook.file_name] = ebook

    def open_ebook(self, file_name):
        self._ebooks[file_name].show()


if __name__ == '__main__':
    library = Library()
    file_names = ['a', 'b', 'c']
    for file_name in file_names:
        library.add(
            LoggingEBookProxy(file_name))  # We can use EBookProxy instead of LoggingEbookProxy (Open-Closed principle)

    library.open_ebook('a')
    library.open_ebook('b')
