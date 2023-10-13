from util.store import Store
from page.connections import Connections
from page.chat import Chat

from textual.app import App
from textual.binding import Binding
from textual.widgets import Header, ContentSwitcher, Footer, Placeholder, DataTable
from textual.containers import Horizontal, ScrollableContainer, Vertical

# Create a new app
class MP(App):
  TITLE = "ModelPrompter 0.0.1"
  CSS_PATH = "./css/app.tcss"
  BINDINGS = [
    Binding("ctrl+b", "toggle_navigation", "Toggle Sidebar")
  ]



  def __init__(self):
    super().__init__()
    self.store = Store(self, 'config.json')
    self.route = self.store.get('current_route', 'connections')
    self.logs = []



  # Compose the layout
  def compose(self):
    yield Header()
    with Horizontal(id='main'):
      with ScrollableContainer(id='navigation-wrap', classes='sidebar mt0'):
        yield DataTable(id='navigation')
      with ContentSwitcher(id='router', initial=self.route):
        yield Connections(id='connections', app=self)
        yield Chat(id='chat', app=self)
    yield Footer()



  # Setup DataTable
  def on_mount(self):
    table = self.query_one('#navigation')
    table.add_column('Navigation', width=23)
    table.add_row('Connections')
    table.add_row('Chat')


  # Toggle the sidebar
  def action_toggle_navigation(self):
    sidebar = self.query_one('#navigation-wrap')
    sidebar.toggle_class('hidden')


  # Log messages to the onscreen terminal
  def print(self, message):
    self.logs.append(message)
    self.refresh()



  # Simple router
  def goto(self, route):
    self.store.set('current_route', route)
    self.query_one('#router').current = route = self.route = route





# Run the app
if __name__ == "__main__":
  MP().run()    