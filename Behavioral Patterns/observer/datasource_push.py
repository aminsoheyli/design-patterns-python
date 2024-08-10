from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, value):
        pass


class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, value):
        for observer in self.observers:
            observer.handle(value)


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
        self.notify_observers(new_value)


class SpreadSheet(Observer):
    def update(self, value):
        print(f'SpreadSheet got notified: {value}')


class Chart(Observer):
    def update(self, value):
        print(f'Chart got updated: {value}')


if __name__ == '__main__':
    datasource = DataSource()
    sheet1 = SpreadSheet()
    sheet2 = SpreadSheet()
    chart = Chart()

    datasource.add_observer(sheet1)
    datasource.add_observer(sheet2)
    datasource.add_observer(chart)

    datasource.value = 5
    datasource.remove_observer(sheet1)
    print('\n')
    datasource.value = 7
