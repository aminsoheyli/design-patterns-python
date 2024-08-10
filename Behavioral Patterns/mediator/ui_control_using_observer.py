# Implementing mediator pattern using observer pattern

from abc import ABC, abstractmethod


# Observer
class EventHandler(ABC):
    @abstractmethod
    def handle(self, control):
        pass


class UIControl(ABC):
    def __init__(self):
        self.event_handlers = []

    # Attach
    def add_event_handler(self, observer):
        self.event_handlers.append(observer)

    # Notify observers
    def _notify_event_handlers(self):
        for event_handler in self.event_handlers:
            event_handler.handle(self)


class ListBox(UIControl):
    def __init__(self):
        super().__init__()
        self._selection = ''

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value):
        self._selection = value
        self._notify_event_handlers()


class TextBox(UIControl):
    def __init__(self):
        super().__init__()
        self._content = ''

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self._notify_event_handlers()


class Button(UIControl):
    def __init__(self):
        super().__init__()
        self._is_enabled = False

    @property
    def is_enabled(self):
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value):
        self._is_enabled = value
        self._notify_event_handlers()


class ArticleDialogBox(EventHandler):
    def __init__(self):
        self.article_list_box = ListBox()
        self.title_text_box = TextBox()
        self.save_button = Button()
        # Subscribe to publisher
        self.article_list_box.add_event_handler(self)
        self.title_text_box.add_event_handler(self)

    def handle(self, control):
        if control == self.article_list_box:
            self.article_selected()
        elif control == self.title_text_box:
            self.title_changed()

    def simulate_user_interaction(self):
        def show_values():
            print(f'TextBox: {self.title_text_box.content}')
            print(f'Button: {self.save_button.is_enabled}')

        self.article_list_box.selection = 'Article 1'
        show_values()
        self.title_text_box.content = ''
        show_values()
        self.title_text_box.content = 'Article 2'
        show_values()

    def article_selected(self):
        self.title_text_box.content = self.article_list_box.selection
        self.save_button.is_enabled = True

    def title_changed(self):
        is_empty = len(self.title_text_box.content) == 0
        self.save_button.is_enabled = not is_empty


if __name__ == '__main__':
    dialog = ArticleDialogBox()
    dialog.simulate_user_interaction()
