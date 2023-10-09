from util.store import Store
from util.router import Router

from textual.app import App
from textual.binding import Binding
from textual.widgets import Header, Button, Placeholder, Footer
from textual.containers import ScrollableContainer, Horizontal

# Create a new app
class MP(App):
  TITLE = "ModelPrompter"
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
    with Horizontal():
      with ScrollableContainer():
        yield from self.router.Yield()
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