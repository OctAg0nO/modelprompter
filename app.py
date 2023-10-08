from textual.app import App
from textual.widgets import Header, Placeholder
from textual.containers import ScrollableContainer, Horizontal, Vertical

# Create a new app
class MP(App):
  TITLE = "ModelPrompter"
  CSS_PATH = "app.css"

  def compose(self):
    yield Header(show_clock=True)
    with Horizontal():
      with ScrollableContainer():
        yield Placeholder("Hello, world!")
      with ScrollableContainer():
        yield Placeholder("Hello, world!")

# Run the app
if __name__ == "__main__":
  MP().run()    