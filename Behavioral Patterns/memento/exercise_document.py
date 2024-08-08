class Document:
    def __init__(self, content='', font_name='', font_size=0):
        self._content = content
        self._font_name = font_name
        self._font_size = font_size

    def create_state(self):
        return DocumentState(self._content, self._font_name, self._font_size)

    def restore(self, state):
        self.content = state.content
        self.font_name = state.font_name
        self.font_size = state.font_size

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def font_name(self):
        return self._font_name

    @font_name.setter
    def font_name(self, value):
        self._font_name = value

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        self._font_size = value

    def __str__(self):
        return f"Document(content='{self._content}', font_name='{self._font_name}', font_size={self._font_size})"


class DocumentState:
    def __init__(self, content, font_name, font_size):
        self.content = content
        self.font_name = font_name
        self.font_size = font_size


class History:
    def __init__(self):
        self.states = []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        return self.states.pop()


if __name__ == '__main__':
    document = Document('Lorem Ipsum', 'fira code', 18)
    history = History()
    history.push(document.create_state())
    document.content = 'new text'
    print(document)
    document.restore(history.pop())
    print(document)
