from abc import ABC, abstractmethod


class ChatClient:
    def __init__(self, encryptor):
        self.encryption_algorithm: EncryptionAlgorithm = encryptor

    def send(self, message):
        encrypted_text = self.encryption_algorithm.encrypt(message)
        print("Sending the encrypted message...")


class UnsupportedOperationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class EncryptionAlgorithm(ABC):
    @abstractmethod
    def encrypt(self, message):
        pass


class AES(EncryptionAlgorithm):
    def encrypt(self, message):
        print("Encrypting message using AES")
        return "encrypted text by AES"


class DES(EncryptionAlgorithm):
    def encrypt(self, message):
        print("Encrypting message using DES")
        return "encrypted text by DES"


if __name__ == '__main__':
    client = ChatClient(AES())
    client.send("Hello world")
