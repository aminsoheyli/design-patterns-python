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


class ContactForm:
    def render(self, theme: Theme):
        if theme == Theme.Ant:
            AntTextBox().render()
            AntButton().render()
        elif theme == Theme.MATERIAL:
            MaterialTextBox().render()
            MaterialButton().render()
