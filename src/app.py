from util.store import Store
from util.router import Router

from textual.app import App
from textual.binding import Binding
from textual.widgets import Header, ContentSwitcher, Footer

# Create a new app
class MP(App):
  TITLE = "ModelPrompter 0.0.1"
  CSS_PATH = "./css/app.css"

  def __init__(self):
    self.router = Router(self, 'connections')
    super().__init__()
    self.store = Store(self, 'config.json')
    self.logs = []

  # Log
  def print(self, message):
    self.logs.append(message)
    self.refresh()

  # Compose the layout
  def compose(self):
    yield Header()
    with ContentSwitcher(initial=self.router.route):
      yield from self.router.compose()
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