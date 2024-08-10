from abc import ABC, abstractmethod


class HtmlNode(ABC):
    @abstractmethod
    def execute(self, operation):
        pass


class HeadingNode(HtmlNode):
    def execute(self, operation):
        operation.apply(self)


class AnchorNode(HtmlNode):
    def execute(self, operation):
        operation.apply(self)


class Operation(ABC):
    @abstractmethod
    def apply(self, heading: HeadingNode = None, anchor: AnchorNode = None):
        pass


class HighlightOperation(Operation):
    def apply(self, heading: HeadingNode = None, anchor: AnchorNode = None):
        if heading is not None:
            print("Highlight-heading")
        if anchor is not None:
            print("Highlight-anchor")


class PlainTextOperation(Operation):
    def apply(self, heading: HeadingNode = None, anchor: AnchorNode = None):
        if heading is not None:
            print("text-heading")
        if anchor is not None:
            print("text-anchor")


class HtmlDocument:
    def __init__(self):
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)

    def execute(self, operation: Operation):
        for node in self.nodes:
            node.execute(operation)


if __name__ == '__main__':
    document = HtmlDocument()
    document.add(HeadingNode())
    document.add(AnchorNode())
    document.execute(HighlightOperation())
    document.execute(PlainTextOperation())
    # operations = [HighlightOperation(), PlainTextOperation()]
    # for operation in operations:
    #     document.execute(operation)
