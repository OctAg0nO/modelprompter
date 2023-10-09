from textual.widgets import Placeholder
from textual.containers import ScrollableContainer, Horizontal

class Connections:
  def View(self):
    with ScrollableContainer():
      yield Placeholder("test")