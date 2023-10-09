from util.store import Store
from util.router import Router

from textual.app import App
from textual.widgets import Header, Button, Placeholder, Footer
from textual.containers import ScrollableContainer, Horizontal

# Create a new app
class MP(App):
  TITLE = "ModelPrompter"
  CSS_PATH = "./css/app.css"

  def __init__(self):
    super().__init__()
    store = Store(self, '../config.json')
    router = Router(self, '/')

  # Compose the layout
  def compose(self):
    yield Header()
    with Horizontal():
      with ScrollableContainer(id="leftSidebar"):
        yield Button("Settings")
      with ScrollableContainer():
        yield Placeholder("Content area")
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