from util.helpers import snake, desnake
from util.store import Store
from page.connections import Connections
from page.chat import Chat

from textual import on
from textual.app import App
from textual.binding import Binding
from textual.widgets import Header, ContentSwitcher, Footer, Placeholder, DataTable
from textual.containers import Horizontal, ScrollableContainer, Vertical

# Create a new app
class MP(App):
  TITLE = "ModelPrompter 0.0.1"
  CSS_PATH = "./css/app.tcss"
  BINDINGS = [
    Binding("ctrl+b", "toggle_navigation", "Toggle Sidebar"),
    Binding('escape', 'close_navigation', 'Close Sidebar', show=False)
  ]
  logs = []



  def __init__(self):
    super().__init__()
    self.store = Store(self, 'config.json', {
      'current_connection': None,
      'current_route': 'connections',
      'connections': [],
      'current_channel': None,
    })
    self.route = self.store.get('current_route', 'connections')
    self.logs = []
  



  # Compose the layout
  def compose(self):
    yield Header()
    with Horizontal(id='main'):
      with ScrollableContainer(id='navigation-wrap', classes='sidebar mt0'):
        yield DataTable(id='navigation', cursor_type="row", zebra_stripes=True)
      with ContentSwitcher(id='router', initial=self.route):
        yield Connections(id='connections', app=self)
        yield Chat(id='chat', app=self)
    yield Footer()



  # Handle Nav routes
  @on(DataTable.RowSelected, '#navigation')
  def on_navigation_selected(self, event):
    nav = self.query_one('#navigation')
    route = snake(nav.get_row_at(event.cursor_row)[0])
    self.goto(route)



  # Setup DataTable
  def on_mount(self):
    table = self.query_one('#navigation')
    table.add_column('Navigation', width=23)
    table.add_row('Connections')
    table.add_row('Chat')

    # Find the route in the tabe with the same name
    route = desnake(self.route)
    # loop through the rows and find the index of the route
    for i, row in enumerate(table.rows):
      nav = table.get_cell_at([i, 0]).lower()
      if (nav == route):
        table.move_cursor(row=i)
        break
    
    self.action_toggle_navigation()



  # Toggle the sidebar
  def action_toggle_navigation(self):
    sidebar = self.query_one('#navigation-wrap')
    sidebar.toggle_class('hidden')
    self.query_one('#navigation').focus()



  # Close the sidebar
  def action_close_navigation(self):
    sidebar = self.query_one('#navigation-wrap')
    sidebar.add_class('hidden')


  # Log messages to the onscreen terminal
  def print(self, message):
    self.logs.append(message)



  # Simple router
  def goto(self, route):
    self.store.set('current_route', route)
    self.query_one('#router').current = route = self.route = route
    self.query_one(f'#router #{route}').on_mount()





# Run the app
if __name__ == "__main__":
  MP().run()    