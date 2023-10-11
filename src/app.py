from util.store import Store
from page.connections import Connections
from page.chat import Chat

from textual.app import App
from textual.widgets import Header, ContentSwitcher, Footer, Placeholder

# Create a new app
class MP(App):
  TITLE = "ModelPrompter 0.0.1"
  CSS_PATH = "./css/app.tcss"

  def __init__(self):
    super().__init__()
    self.store = Store(self, 'config.json')
    self.route = self.store.get('current_route', 'connections')
    self.logs = []

  # Log messages to the onscreen terminal
  def print(self, message):
    self.logs.append(message)
    self.refresh()

  # Simple router
  def goto(self, route):
    self.store.set('current_route', route)
    self.query_one('#router').current = route = self.route = route

  # Compose the layout
  def compose(self):
    yield Header()
    with ContentSwitcher(id='router', initial=self.route):
      yield Connections(id='connections', app=self)
      yield Chat(id='chat', app=self)
    yield Footer()

# Run the app
if __name__ == "__main__":
  MP().run()    