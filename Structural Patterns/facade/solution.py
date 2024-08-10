class Message:
    def __init__(self, content):
        self.content = content


class Connection:
    def disconnect(self):
        pass


class AuthToken:
    pass


class NotificationServer:
    # connect() -> Connection
    # authenticate(appID, key) -> authToken
    # send(authToken, message, target)
    # conn.disconnect()
    def connect(self, ip_address) -> Connection:
        return Connection()

    def authenticate(self, appID, key):
        return AuthToken()

    def send(self, authToken, message, target):
        print('Sending a message')


class NotificationService:
    def send(self, message, target):
        server = NotificationServer()
        connection = server.connect('ip')
        auth_token = server.authenticate('appID', 'key')
        server.send(auth_token, Message(message), target)
        connection.disconnect()


if __name__ == '__main__':
    service = NotificationService()
    service.send('Hello World', 'target')
