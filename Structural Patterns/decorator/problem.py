class CloudStream:
    def write(self, data):
        print(f'Storing {data}')


class EncryptedCloudStream(CloudStream):
    def write(self, data):
        encrypted_data = self.encrypt(data)
        super().write(encrypted_data)

    def encrypt(self, data):
        return '!@#!!!!@*(&$!@*$(!'


class CompressedCloudStream(CloudStream):
    def write(self, data):
        compressed_data = self.compress(data)
        super().write(compressed_data)

    def compress(self, data):
        return data[0:5]


if __name__ == '__main__':
    cloud_stream = CloudStream()
    cloud_stream.write('Some data')
