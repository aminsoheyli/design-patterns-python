from abc import ABC, abstractmethod

# Basic Remote Control (turnOn, turnOff)
# Advanced Remote Control (setChannel)
# Movie Remote Control (play, pause, rewind)

# Problem:
# ---------------------------------------------------------------------
#    RemoteControl  -> Feature class
#      SonyRemoteControl
#      SamsungRemoteControl
#      AdvancedRemoteControl    -> Feature class
#          SonyAdvancedRemoteControl
#          SamsungAdvancedRemoteControl
#
#      2 types of remote controls, 2 new company -> 2 * 2 new classes
#      n types of remote controls, m new company -> n * m new classes
# ---------------------------------------------------------------------
''' 
  Solution:
---------------------------------------------------------------------
    In these problems we have two dimension of classes that grows: Feature dimension and Implementation dimension
'''


class Device(ABC):
    @abstractmethod
    def turn_on(self): pass

    @abstractmethod
    def turn_off(self): pass

    @abstractmethod
    def set_channel(self, number): pass


class SonyTV(Device):

    def turn_on(self):
        print('Sony: turn on')

    def turn_off(self):
        print('Sony: turn off')

    def set_channel(self, number):
        print('Sony: set channel')


class SamsungTV(Device):

    def turn_on(self):
        print('Samsung: turn on')

    def turn_off(self):
        print('Samsung: turn off')

    def set_channel(self, number):
        print('Samsung: set channel')


class RemoteControl:
    def __init__(self, device: Device):
        self.device: Device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()


class AdvancedRemoteControl(RemoteControl):
    def __init__(self, device: Device):
        super().__init__(device)

    def set_channel(self, number):
        self.device.set_channel(number)


if __name__ == '__main__':
    remote_control = AdvancedRemoteControl(SamsungTV())
    remote_control.turn_on()
