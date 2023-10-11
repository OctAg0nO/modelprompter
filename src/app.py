from util.store import Store
from page.connections import Connections

from textual.app import App
from textual.widgets import Header, ContentSwitcher, Footer, Placeholder

# Create a new app
class MP(App):
  TITLE = "ModelPrompter 0.0.1"
  CSS_PATH = "./css/app.tcss"

  def __init__(self):
    self.route = 'connections'
    super().__init__()
    self.store = Store(self, 'config.json')
    self.logs = []

  # Log messages to the onscreen terminal
  def print(self, message):
    self.logs.append(message)
    self.refresh()

  # Simple router
  def goto(self, route):
    self.route = route
    self.refresh()

  # Compose the layout
  def compose(self):
    yield Header()
    with ContentSwitcher(initial=self.route):
      yield Connections(id='connections', app=self)
    yield Footer()

  """
  - Check if ../../config.json exists
  - If it doesn't, redirect route to /settings/connections/new
  """
  async def on_mount(self):
    pass

# Run the app
if __name__ == "__main__":
  MP().run()    