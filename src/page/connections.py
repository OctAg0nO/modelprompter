from textual.widgets import Label, Placeholder, DataTable, Button, Input, Markdown, Static
from textual.containers import ScrollableContainer, Horizontal, Vertical

class Connections(Static):
  # def __init__(self):
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
        yield Input(value='')
        yield Label('Model')
        yield Input(value='gpt4')
        yield Label('API Type')
        yield Input(value='open_ai')
        yield Label('API Base')
        yield Input(value='https://api.openai.com/v1/chat/completions')
        yield Label('Max tokens')
        yield Input(value='4096')
        yield Button(label='Add new connection', variant='primary')
      with Vertical():
        with ScrollableContainer():
          yield Placeholder('Info/News')
        with ScrollableContainer():
          yield DataTable()
          # yield Button(label='Submit', variant='primary')

    # table = self.query_one(DataTable)
    # table.add_columns(*ROWS[0])
    # table.add_rows(ROWS[1:])