from abc import ABC, abstractmethod


class Stream(ABC):
    @abstractmethod
    def write(self, data):
        pass


class CloudStream(Stream):
    def write(self, data):
        print(f'Storing {data}')


class EncryptedCloudStream(Stream):
    def __init__(self, stream: Stream):
        self.stream: Stream = stream

    def write(self, data):
        encrypted_data = self.encrypt(data)
        self.stream.write(encrypted_data)

    def encrypt(self, data):
        return '!@#!!!!@*(&$!@*$(!'


class CompressedCloudStream(Stream):
    def __init__(self, stream: Stream):
        self.stream: Stream = stream

    def write(self, data):
        compressed_data = self.compress(data)
        self.stream.write(compressed_data)

    def compress(self, data):
        return data[0:5]


def store_credit_card(stream: Stream):
    stream.write('12391-190123-14289')


if __name__ == '__main__':
    store_credit_card(EncryptedCloudStream(CompressedCloudStream(CloudStream())))
