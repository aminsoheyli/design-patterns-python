from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()


class DataSource(Observable):
    def __init__(self):
        super().__init__()
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self.notify_observers()


class SpreadSheet(Observer):
    def __init__(self, datasource):
        self._datasource = datasource

    def update(self):
        print(f'SpreadSheet got notified: {self._datasource.value}')


class Chart(Observer):
    def __init__(self, datasource):
        self._datasource = datasource

    def update(self):
        print(f'Chart got updated: {self._datasource.value}')


if __name__ == '__main__':
    datasource = DataSource()
    sheet1 = SpreadSheet(datasource)
    sheet2 = SpreadSheet(datasource)
    chart = Chart(datasource)

    datasource.add_observer(sheet1)
    datasource.add_observer(sheet2)
    datasource.add_observer(chart)

    datasource.value = 5
    datasource.remove_observer(sheet1)
    print('\n')
    datasource.value = 7
