from textual.app import App
from textual.widgets import Header, Button, Placeholder, Footer
from textual.containers import ScrollableContainer, Horizontal

# Create a new app
class MP(App):
  TITLE = "ModelPrompter"
  CSS_PATH = "app.css"

  def compose(self):
    yield Header()
    with Horizontal():
      with ScrollableContainer(id="leftSidebar"):
        yield Placeholder("Sidebar area")
      with ScrollableContainer():
        yield Placeholder("Content area")
    yield Footer()

# Run the app
if __name__ == "__main__":
  MP().run()    