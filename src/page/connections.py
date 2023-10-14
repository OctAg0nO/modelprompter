import uuid

from textual import on
from textual.binding import Binding
from textual.widgets import Label, DataTable, Button, Input, Static
from textual.containers import ScrollableContainer, Horizontal, Vertical

COLUMNS = ["Connection", "Model", "MaxTokens", "Notes"]

class Connections(Static):
  app = {}
  BINDINGS = [
    Binding("f5", "reload_config", "Reload config"),
  ]



  def __init__(self, app, id):
    super().__init__()
    self.app = app
    self.id = id



  def compose(self):
    # 2 column layout, 1 with a Placeholder and one with a DataTable
    # NOTE: id must === app.route
    with Horizontal(id='route-connections'):
      with ScrollableContainer(classes='sidebar mt0'):
        # yield Markdown("""## New Connection""", classes="mt0")
        yield Label('API Key*')
        yield Input(id='connections-new-key', value='', password=True)
        yield Label('Model*')
        yield Input(id='connections-new-model', value='gpt4')
        yield Label('API Type')
        yield Input(value='open_ai', id='connections-new-api-type')
        yield Label('API Base')
        yield Input(value='https://api.openai.com/v1', id='connections-new-api-base')
        yield Label('Max tokens')
        yield Input(value='4096', id='connections-new-max-tokens')
        yield Button(id='connections-new-btn', label='Add new connection', variant='primary')
      with Vertical():
        with ScrollableContainer(classes='pl1'):
          yield DataTable(id='connections-table', cursor_type="row", zebra_stripes=True)



  def on_mount(self):
    """
    - Sets up the columns
    - Loads initial data
    - Selects the current row
    """
    if (self.app.route != 'connections'):
      return

    table = self.query_one('#connections-table')
    table.clear(columns=True)
    table.add_columns(*COLUMNS)
    table.add_rows(self.dbToRows(self.app.store.get('connections', [])))
    self.select_row_by_id(self.app.store.get('current_connection'))



  def action_reload_config(self):
    """Reloads the config from the file"""
    table = self.query_one('#connections-table')
    table.clear()
    self.app.store.data = self.app.store.load_data()
    table.add_rows(self.dbToRows(self.app.store.get('connections', [])))
    self.select_row_by_id(self.app.store.get('current_connection'))



  def dbToRows(self, data, keys=["name", "model", "max_tokens", "notes"]):
    # Loop through and extract the keys from each connection
    return [list(map(lambda key: connection.get(key), keys)) for connection in data]



  @on(Button.Pressed, '#connections-new-btn')
  def create_connection(self):
    """Adds a new connection to the DataTable"""
    table = self.query_one('#connections-table')
    key = self.query_one('#connections-new-key').value
    model = self.query_one('#connections-new-model').value
    api_type = self.query_one('#connections-new-api-type').value
    api_base = self.query_one('#connections-new-api-base').value
    max_tokens = self.query_one('#connections-new-max-tokens').value

    ID = uuid.uuid4().hex
    table.add_row('Untitled', model, max_tokens, '', key=ID)
    self.app.store.append('connections', {
      'id': ID,
      'name': 'Untitled',
      'key': key,
      'model': model,
      'api_type': api_type,
      'api_base': api_base,
      'max_tokens': max_tokens,
      'notes': ''
    })
    self.app.store.set('current_connection', ID)
    self.select_row_by_id(ID)
    self.app.goto('chat')



  def select_row_by_id(self, ID):
    """
    - Selects the cursor by ID
    - If ID is None, deselects the cursor
    """
    table = self.query_one('#connections-table')
    connections = self.app.store.get('connections', [])
    # Find the index of the connection with ID
    index = next((index for (index, d) in enumerate(connections) if d["id"] == ID), None)
    table.move_cursor(row=index)
    self.app.store.set('current_connection', ID)



  @on(DataTable.RowSelected, '#connections-table')
  def on_row_selected(self, event):
    """Sets the current_connection to the ID of the selected row"""
    connections = self.app.store.get('connections', [])
    self.select_row_by_id(connections[event.cursor_row]['id'])
    self.app.goto('chat')