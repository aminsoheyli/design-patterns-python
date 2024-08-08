from abc import ABC, abstractmethod


class HtmlDocument:
    def __init__(self):
        self._content = ''

    def make_bold(self):
        self._content = f'<b>{self._content}</b>'

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class UndoableCommand(Command):
    @abstractmethod
    def unexecute(self):
        pass


class History:
    def __init__(self):
        self._commands = []

    def push(self, command: Command):
        self._commands.append(command)

    def pop(self):
        return self._commands.pop()

    def size(self):
        return len(self._commands)


class BoldCommand(UndoableCommand):
    def __init__(self, document: HtmlDocument, history: History):
        self.prev_content = ''
        self.document = document
        self.history = history

    def execute(self):
        self.prev_content = self.document.content
        self.document.make_bold()
        self.history.push(self)

    def unexecute(self):
        self.document.content = self.prev_content


class UndoCommand(Command):
    def __init__(self, history: History):
        self.history = history

    def execute(self):
        if self.history.size() > 0:
            history.pop().unexecute()


if __name__ == '__main__':
    history = History()
    document = HtmlDocument()
    document.content = 'Hello World'

    bold_command = BoldCommand(document, history)
    bold_command.execute()
    print(document.content)

    undo_command = UndoCommand(history)
    undo_command.execute()
    print(document.content)
