from textual.widgets import Placeholder
from page.connections import Connections

class Router:
  def __init__(self, app, route):
    self.app = app
    self.route = route
    self.components = []

  def goto(self, route):
    self.route = route

  def Yield(self):
    if (self.route == 'connections'):
      yield from Connections().View()
    else:
      yield Placeholder('🐞 404\n\nRoute: ' + str(self.route))