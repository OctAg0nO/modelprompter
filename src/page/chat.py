from textual.widgets import Static, Placeholder, Input
from textual.containers import ScrollableContainer, Horizontal, Vertical

class Chat(Static):
  app = {}
  BINDINGS = []
  
  def __init__(self, app, id):
    super().__init__()
    self.app = app
    self.id = id

  def compose(self):
    with Horizontal():
      with ScrollableContainer(classes='sidebar mt0'):
        yield Placeholder('Sidebar')
      with Vertical(classes='pl1'):
        with ScrollableContainer():
          yield Placeholder('Messages')
        with Horizontal(id='chat-input-wrap', classes='p0'):
          yield Input(value='', id='chat-input', placeholder='Type your prompt here...')

  def on_mount(self):
    self.query_one('#chat-input').focus()