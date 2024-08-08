from gui import Command


class ResizeCommand(Command):

    def execute(self):
        print('Resize')


class BlackAndWhiteCommand(Command):

    def execute(self):
        print('Black and white')


class CompositeCommand(Command):
    def __init__(self):
        self.commands = []

    def add(self, command: Command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()


if __name__ == '__main__':
    composite = CompositeCommand()
    composite.add(ResizeCommand())
    composite.add(BlackAndWhiteCommand())
    composite.execute()
