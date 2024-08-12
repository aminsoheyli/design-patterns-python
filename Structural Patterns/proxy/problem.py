class EBook:
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
        library.add(EBook(file_name))

    library.open_ebook('a')
