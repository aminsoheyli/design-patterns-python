from abc import ABC, abstractmethod


class Button:
    def __init__(self, command):
        self._label = ''
        self.command: Command = command

    def click(self):
        self.command.execute()

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CustomerService:
    def add_customer(self):
        print("Add customer")


class AddCustomerCommand(Command):
    def __init__(self, service):
        self.service: CustomerService = service

    def execute(self):
        self.service.add_customer()


if __name__ == '__main__':
    service = CustomerService()
    command = AddCustomerCommand(service)
    button = Button(command)
    button.click()
