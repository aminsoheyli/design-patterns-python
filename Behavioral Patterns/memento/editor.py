class Editor:
    def __init__(self):
        self._content = ""

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        # self.prevState.append(self._content)
        self._content = content

    def createState(self):
        return EditorState(self.content)

    def restore(self, state):
        self.content = state.content


class EditorState:
    def __init__(self, content):
        self.content = content


class History:
    def __init__(self):
        self.states = []

    def push(self, state):
        self.states.append(state)

    def pop(self):
        return self.states.pop()

if __name__ == '__main__':
    editor = Editor()
    history = History()
    editor.content = "A"
    history.push(editor.createState())
    editor.content = "B"
    history.push(editor.createState())
    editor.content = "C"
    editor.restore(history.pop())
    print(editor.content) # B