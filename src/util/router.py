from textual.widgets import Placeholder
from page.connections import Connections

class Router:
  def __init__(self, app, route):
    self.app = app
    self.route = route

  def goto(self, route):
    self.route = route
    self.app.refresh()

  def compose(self):
    if (self.route == 'connections'):
      yield from Connections(self).compose()
    else:
      yield Placeholder('🐞 404\n\nRoute: ' + str(self.route))