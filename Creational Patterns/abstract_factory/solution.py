from abc import ABC, abstractmethod
from enum import Enum


class Widget(ABC):
    @abstractmethod
    def render(self): pass


class Button(Widget):
    @abstractmethod
    def render(self): pass


class TextBox(Widget):
    @abstractmethod
    def render(self): pass


class MaterialButton(Button):
    def render(self):
        print('Material Button')


class MaterialTextBox(TextBox):
    def render(self):
        print('Material TextBox')


class AntButton(Button):
    def render(self):
        print('Ant Button')


class AntTextBox(TextBox):
    def render(self):
        print('Ant TextBox')


class Theme(Enum):
    MATERIAL = 1
    ANT = 2


class WidgetFactory(ABC):
    @abstractmethod
    def createButton(self): pass

    @abstractmethod
    def createTextBox(self): pass


class MaterialWidgetFactory(WidgetFactory):

    def createButton(self):
        return MaterialButton()

    def createTextBox(self):
        return MaterialTextBox()


class AntWidgetFactory(WidgetFactory):
    def createButton(self):
        return AntButton()

    def createTextBox(self):
        return AntTextBox()


class ContactForm:
    def render(self, factory: WidgetFactory):
        factory.createTextBox().render()
        factory.createButton().render()


if __name__ == '__main__':
    ContactForm().render(MaterialWidgetFactory())
