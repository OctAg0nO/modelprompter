import uuid

from textual import on
from textual.binding import Binding
from textual.widgets import Label, DataTable, Button, Input, Markdown, Static
from textual.containers import ScrollableContainer, Horizontal, Vertical

COLUMNS = ["Connection", "Model", "MaxTokens", "Notes"]

class Connections(Static):
  app = {}

  BINDINGS = [  
    Binding('Enter', 'add_or_select_connection', 'Add/select connection'),
  ]
  
  def __init__(self, id, app):
    super().__init__()
    self.id = id
    self.app = app
    
  def compose(self):
    # 2 column layout, 1 with a Placeholder and one with a DataTable
    # NOTE: id must === app.route
    with Horizontal(id='route-connections'):
      with ScrollableContainer(classes='sidebar'):
        yield Markdown("""\
## Connections
Connections are saved into `./config.json`.
""", classes="mt0")
        yield Label('API Key*')
        yield Input(id='connections-new-key', value='', password=True)
        yield Label('Model*')
        yield Input(id='connections-new-model', value='gpt4')
        yield Label('API Type')
        yield Input(value='open_ai', id='connections-new-api-type')
        yield Label('API Base')
        yield Input(value='https://api.openai.com/v1/chat/completions', id='connections-new-api-base')
        yield Label('Max tokens')
        yield Input(value='4096', id='connections-new-max-tokens')
        yield Button(id='connections-new-btn', label='Add new connection', variant='primary')
      with Vertical():
        with ScrollableContainer():
          yield DataTable(id='connections-table', cursor_type="row", zebra_stripes=True)

  def on_mount(self):
    table = self.query_one('#connections-table')
    table.add_columns(*COLUMNS)
    table.add_rows(self.dbToRows(self.app.store.get('connections', [])))

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

    table.add_row('Untitled', model, max_tokens, '')
    ID = uuid.uuid4().hex
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
    # self.select_row_by_id(ID)
    # self.app.goto('prompt')

  def add_or_select_connection(self):
    """
    Query the DataTable and check if it's focused
    If it is, we'll select it otherwise we'll submit the form as is
    """
    table = self.query_one('#connections-table')
    self.create_connection()

    # if (table.focused):
    #   self.app.goto('prompt')
    # else:
    #   self.create_connection()