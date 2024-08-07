class BrowseHistory:
    def __init__(self):
        self.__urls = []

    def push(self, url):
        self.__urls.append(url)

    def pop(self):
        return self.__urls.pop()

    def createIterator(self):
        return self.ListIterator(self)

    class ListIterator:
        def __init__(self, history):
            self.history = history
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < len(self.history._BrowseHistory__urls):
                result = self.history._BrowseHistory__urls[self.index]
                self.index += 1
                return result
            else:
                raise StopIteration


if __name__ == "__main__":
    history = BrowseHistory()
    history.push("A")
    history.push("B")
    history.push("C")

    iterator = history.createIterator()
    for url in iterator:
        print(url)
