# State Pattern

If you have a few decision-making branches in a single method like as following example, don't use the state pattern.
```python
class Stopwatch:
    def __init__(self):
        self.is_running = False

    def click(self):
        if self.is_running:
            self.is_running = False
            print("Stopped")
        else:
            self.is_running = True
            print("Running")
```
Use it only if you have the same decision-making statements in multiple methods like as: 

```python
from enum import Enum


class ToolType(Enum):
    SELECTION = 1
    BRUSH = 2
    ERASER = 3


class Canvas:
    def __init__(self):
        self._current_tool: ToolType = None

    def mouseDown(self):
        if self._current_tool == ToolType.SELECTION:
            print("Selection icon")
        elif self._current_tool == ToolType.BRUSH:
            print("Brush icon")
        elif self._current_tool == ToolType.ERASER:
            print("Eraser icon")

    def mouseUp(self):
        if self._current_tool == ToolType.SELECTION:
            print("Draw dashed rectangle")
        elif self._current_tool == ToolType.BRUSH:
            print("Draw line")
        elif self._current_tool == ToolType.ERASER:
            print("Erase something")
```