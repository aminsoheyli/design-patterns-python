from abc import ABC, abstractmethod


class HttpRequest:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password


class Handler(ABC):
    def __init__(self, next: None):
        self.next: Handler = next

    def handle(self, request: HttpRequest):
        if self.do_handle(request):
            return
        if self.next is not None:
            self.next.handle(request)

    @abstractmethod
    def do_handle(self, request: HttpRequest) -> bool:
        pass


class Authenticator(Handler):
    def __init__(self, next: Handler):
        super().__init__(next)

    def do_handle(self, request: HttpRequest) -> bool:
        print('Authentication')
        is_valid = request.username == 'admin' and request.password == '1234'
        return not is_valid


class Logger(Handler):
    def __init__(self, next: Handler):
        super().__init__(next)

    def do_handle(self, request: HttpRequest):
        print('Logging')
        return False


class Compressor(Handler):
    def __init__(self, next: Handler = None):
        super().__init__(next)

    def do_handle(self, request: HttpRequest):
        print("Compression")
        return True


class WebServer:
    def __init__(self, handler: Handler):
        self.handler = handler

    def handle(self, request: HttpRequest):
        # Authentication
        # Logging
        # Compression
        self.handler.handle(request)
        pass


if __name__ == '__main__':
    # authenticator -> logger -> compressor
    # compressor = Compressor(None)
    # logger = Logger(compressor)
    # authenticator = Authenticator(logger)
    authenticator = Authenticator(Logger(Compressor(None)))
    server = WebServer(authenticator)
    server.handle(HttpRequest('admin', '1234'))
