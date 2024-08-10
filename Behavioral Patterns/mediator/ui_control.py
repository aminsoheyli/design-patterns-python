from abc import ABC, abstractmethod


class UIControl:
    def __init__(self, owner):
        self._owner = owner


class DialogBox(ABC):
    @abstractmethod
    def changed(self, control: UIControl):
        pass


class ListBox(UIControl):
    def __init__(self, owner: DialogBox):
        super().__init__(owner)
        self._selection = ''

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value):
        self._selection = value
        self._owner.changed(self)


class TextBox(UIControl):
    def __init__(self, owner):
        super().__init__(owner)
        self._content = ''

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self._owner.changed(self)


class Button(UIControl):
    def __init__(self, owner):
        super().__init__(owner)
        self._is_enabled = False

    @property
    def is_enabled(self):
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, value):
        self._is_enabled = value
        self._owner.changed(self)


class ArticleDialogBox(DialogBox):
    def __init__(self):
        self.article_list_box = ListBox(self)
        self.title_text_box = TextBox(self)
        self.save_button = Button(self)

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

    def changed(self, control: UIControl):
        if control == self.article_list_box:
            self.article_selected()
        elif control == self.title_text_box:
            self.title_changed()

    def article_selected(self):
        self.title_text_box.content = self.article_list_box.selection
        self.save_button.is_enabled = True

    def title_changed(self):
        is_empty = len(self.title_text_box.content) == 0
        self.save_button.is_enabled = not is_empty


if __name__ == '__main__':
    dialog = ArticleDialogBox()
    dialog.simulate_user_interaction()
