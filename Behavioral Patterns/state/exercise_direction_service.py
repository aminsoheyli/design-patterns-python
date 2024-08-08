from enum import Enum


class DirectionService:
    def __init__(self, travel_mode):
        self._travel_mode: TravelMode = travel_mode

    def get_eta(self):
        self.travel_mode.get_eta()

    def get_direction(self):
        self.travel_mode.get_direction()

    @property
    def travel_mode(self):
        return self._travel_mode

    @travel_mode.setter
    def travel_mode(self, travel_mode):
        self._travel_mode = travel_mode


from abc import ABC, abstractmethod


class TravelMode(ABC):
    @abstractmethod
    def get_eta(self):
        pass

    @abstractmethod
    def get_direction(self):
        pass


class Driving(TravelMode):
    def get_eta(self):
        print("Calculating ETA (driving)")
        return 1

    def get_direction(self):
        print("Calculating Direction (driving)")
        return 1


class Bicycling(TravelMode):
    def get_eta(self):
        print("Calculating ETA (bicycling)")
        return 2

    def get_direction(self):
        print("Calculating Direction (bicycling)")
        return 2


class Transit(TravelMode):
    def get_eta(self):
        print("Calculating ETA (transit)")
        return 3

    def get_direction(self):
        print("Calculating Direction (transit)")
        return 3


class Walking(TravelMode):
    def get_eta(self):
        print("Calculating ETA (walking)")
        return 4

    def get_direction(self):
        print("Calculating Direction (walking)")
        return 4


if __name__ == '__main__':
    direction_service = DirectionService(Driving())
    direction_service.get_eta()
    direction_service.get_direction()
