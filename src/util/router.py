from textual.widgets import Placeholder

class Router:
  def __init__(self, app, route):
    self.app = app
    self.route = route

  def goto(self, route):
    self.route = route

  def View(self):
    """Yields the fields based on the route"""
    yield Placeholder("Content area")