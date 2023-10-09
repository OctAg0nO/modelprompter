from textual.widgets import Label, Placeholder, DataTable, Button, Input, Markdown
from textual.containers import ScrollableContainer, Horizontal, Vertical

# Mock data
ROWS = [
  ("lane", "swimmer", "country", "time"),
  (4, "Joseph Schooling", "Singapore", 50.39),
  (2, "Michael Phelps", "United States", 51.14),
  (5, "Chad le Clos", "South Africa", 51.14),
  (6, "László Cseh", "Hungary", 51.14),
  (3, "Li Zhuhao", "China", 51.26),
  (8, "Mehdy Metella", "France", 51.58),
  (7, "Tom Shields", "United States", 51.73),
  (1, "Aleksandr Sadovnikov", "Russia", 51.84),
  (10, "Darren Burns", "Scotland", 51.84),
]

class Connections:
  def __init__(self, app):
    self.app = app
    pass
  
  def compose(self):
    # 2 column layout, 1 with a Placeholder and one with a DataTable
    # NOTE: id must === app.route
    with Horizontal(id='connections'):
      with ScrollableContainer(classes='sidebar'):
        yield Markdown("""\
## Connections
Connections are saved into `./config.json`.
""")
        yield Input(placeholder='Model*', value='gpt3.5-turbo')
        yield Input(placeholder='API Key*', value='')
        yield Input(placeholder='API Type*', value='open_ai')
        yield Input(placeholder='API Base', value='')
        yield Input(placeholder='Max tokens', value='4096')
        yield Button(label='Add new connection', variant='primary')
      with Vertical():
        with ScrollableContainer():
          yield Placeholder('Info/News')
        with ScrollableContainer():
          yield Placeholder('Connections Grid')
          # yield DataTable()
          # yield Button(label='Submit', variant='primary')

    # table = self.query_one(DataTable)
    # table.add_columns(*ROWS[0])
    # table.add_rows(ROWS[1:])