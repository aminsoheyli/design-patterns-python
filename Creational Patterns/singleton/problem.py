class ConfigManager:
    def __init__(self):
        self.__settings = {}

    def set(self, key, value):
        self.__settings[key] = value

    def get(self, key):
        return self.__settings[key]


if __name__ == '__main__':
    config_manager = ConfigManager()
    config_manager.set('name', 'John')

    other_config_manager = ConfigManager()
    print(other_config_manager.get('name'))
