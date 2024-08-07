from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def next(self):
        pass


class BrowseHistory:
    def __init__(self):
        self.__urls = []

    def push(self, url):
        self.__urls.append(url)

    def pop(self):
        return self.__urls.pop()

    def createIterator(self):
        return self.ListIterator(self)

    class ListIterator(Iterator):
        def __init__(self, history):
            self.history = history
            self.index = 0

        def hasNext(self):
            return self.index < len(self.history._BrowseHistory__urls)

        def current(self):
            return self.history._BrowseHistory__urls[self.index]

        def next(self):
            self.index += 1


if __name__ == "__main__":
    history = BrowseHistory()
    history.push("A")
    history.push("B")
    history.push("C")

    iterator: Iterator = history.createIterator()
    while iterator.hasNext():
        url = iterator.current()
        print(url)
        iterator.next()
