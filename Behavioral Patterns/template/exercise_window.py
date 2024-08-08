class Window:

    def close(self):
        self._on_closing()
        print("Removing the window from the screen")
        self._on_closed()

    def _on_closing(self):
        pass

    def _on_closed(self):
        pass


class ChatWindow(Window):
    def _on_closed(self):
        print('Disconnecting from the server...')


if __name__ == '__main__':
    window = ChatWindow()
    window.close()
