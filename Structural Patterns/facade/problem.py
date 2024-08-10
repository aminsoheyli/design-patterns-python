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


if __name__ == '__main__':
    server = NotificationServer()
    connection = server.connect('ip')
    auth_token = server.authenticate('appID', 'key')
    message = Message('Hello World')
    server.send(auth_token, message, 'target')
    connection.disconnect()
