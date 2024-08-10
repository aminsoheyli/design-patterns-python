from abc import ABC, abstractmethod


# Basic Remote Control (turnOn, turnOff)
# Advanced Remote Control (setChannel)
# Movie Remote Control (play, pause, rewind)

# RemoteControl
#   SonyRemoteControl
#   SamsungRemoteControl
#   AdvancedRemoteControl
#       SonyAdvancedRemoteControl
#       SamsungAdvancedRemoteControl
#
#   2 types of remote controls, 2 new company -> 2 * 2 new classes
#   n types of remote controls, m new company -> n * m new classes
class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self): pass

    @abstractmethod
    def turn_off(self): pass


class AdvancedRemoteControl(RemoteControl):
    @abstractmethod
    def set_channel(self, number): pass


class SonyRemoteControl(RemoteControl):
    def turn_on(self):
        print('Sony: Turn On')

    def turn_off(self):
        print('Sony: Turn Off')


class SonyAdvancedRemoteControl(AdvancedRemoteControl, SonyRemoteControl):
    def set_channel(self, number):
        print('Sony: Set Channel')
