from textual import on
from textual.widgets import Label, DataTable, Button, Input, Markdown, Static
from textual.containers import ScrollableContainer, Horizontal, Vertical

COLUMNS = ["Connection", "Model", "MaxTokens", "Notes"]

class Connections(Static):
  def __init__(self, id, store):
    super().__init__()
    self.id = id
    self.store = store
    
  def compose(self):
    # 2 column layout, 1 with a Placeholder and one with a DataTable
    # NOTE: id must === app.route
    with Horizontal(id='connections'):
      with ScrollableContainer(classes='sidebar'):
        yield Markdown("""\
## Connections
Connections are saved into `./config.json`.
""")
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
          yield DataTable(cursor_type="row", zebra_stripes=True)

  def on_mount(self):
    table = self.query_one(DataTable)
    table.add_columns(*COLUMNS)
    table.add_rows(self.dbToRows(self.store.get('connections', [])))

  def dbToRows(self, data, keys=["name", "model", "max_tokens", "notes"]):
    # Loop through and extract the keys from each connection
    return [list(map(lambda key: connection.get(key), keys)) for connection in data]

  @on(Button.Pressed, '#connections-new-btn')
  def create_connection(self, event):
    """Adds a new connection to the DataTable"""
    table = self.query_one(DataTable)
    key = self.query_one('#connections-new-key').value
    model = self.query_one('#connections-new-model').value
    api_type = self.query_one('#connections-new-api-type').value
    api_base = self.query_one('#connections-new-api-base').value
    max_tokens = self.query_one('#connections-new-max-tokens').value
    # notes = self.query_one('#connections-new-notes').value

    ID = table.add_row('Untitled', model, max_tokens, '').value
    self.store.append('connections', {
      'id': ID,
      'name': 'Untitled',
      'key': key,
      'model': model,
      'api_type': api_type,
      'api_base': api_base,
      'max_tokens': max_tokens,
      'notes': ''
    })