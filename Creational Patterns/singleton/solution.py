class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._settings = {}
        return cls._instance

    def set(self, key, value):
        self._settings[key] = value

    def get(self, key):
        return self._settings[key]


if __name__ == '__main__':
    config_manager = ConfigManager()
    config_manager.set('name', 'John')

    other_config_manager = ConfigManager()
    print(config_manager.get('name'))
