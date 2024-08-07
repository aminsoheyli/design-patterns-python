from enum import Enum
from abc import ABC, abstractmethod, abstractproperty


class Canvas:
    def __init__(self):
        self._current_tool = None

    def mouseDown(self):
        self._current_tool.mouseDown()

    def mouseUp(self):
        self._current_tool.mouseUp()

    @property
    def current_tool(self):
        return self._current_tool

    @current_tool.setter
    def current_tool(self, tool):
        self._current_tool = tool


class Tool(ABC):
    @abstractmethod
    def mouseUp(self):
        pass

    @abstractmethod
    def mouseDown(self):
        pass


class SelectionTool(Tool):
    def mouseDown(self):
        print("Selection icon")

    def mouseUp(self):
        print("Draw dashed rectangle")


class BrushTool(Tool):
    def mouseDown(self):
        print("Brush icon")

    def mouseUp(self):
        print("Draw line")


class EraserTool(Tool):
    def mouseDown(self):
        print("Eraser icon")

    def mouseUp(self):
        print("Erase something")


if __name__ == "__main__":
    canvas = Canvas()
    canvas.current_tool = BrushTool()
    canvas.mouseDown()
    canvas.mouseUp()
    canvas.current_tool = EraserTool()
    canvas.mouseDown()
    canvas.mouseUp()
