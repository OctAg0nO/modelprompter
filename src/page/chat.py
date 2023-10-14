import os
import json
from datetime import datetime

from util.store import Store
from util.helpers import snake

from textual import on
from textual.reactive import reactive
from textual.widgets import Label, Static, Placeholder, Input, DataTable, Markdown
from textual.containers import ScrollableContainer, Horizontal, Vertical

class Chat(Static):
  BINDINGS = []
  app = {}
  store = {}
  channel_list = reactive(list(), always_update=True, init=False)
  active_channel = reactive('', always_update=True, init=False)


  def __init__(self, app, id):
    super().__init__()
    self.app = app
    self.id = id
    self.load_channels()
    self.store = Store(self, f'data/chat/{self.active_channel}.json', {
      'name': 'General',
      'messages': [],
      'api': ''
    })



  def compose(self):
    with Horizontal():
      with ScrollableContainer(id='chat-sidebar', classes='sidebar mt0'):
        yield DataTable(id='chat-channels', cursor_type="row", zebra_stripes=True)
      with Vertical(classes='pl1'):
        with ScrollableContainer(id='chat-messages'):
          pass
        with Horizontal(id='chat-input-wrap', classes='p0'):
          yield Input(value='', id='chat-input', placeholder='Prompt here...')



  def on_mount(self):
    """
    - Focus input
    - Go back to 'connections' if no connection is set    
    - Load channels
    """
    if not self.app.store.get('current_connection'):
      self.app.goto('connections')

    # Load channels
    self.query_one('#chat-channels').add_column('Channels', width=23)
    self.query_one('#chat-channels').add_rows([self.channel_list])
    self.query_one('#chat-input').focus()



  def load_channels(self):
    channel_dir = os.path.join(os.getcwd(), 'data', 'chat')
    # Load all filenames in data/chat into an array
    filenames = [f for f in os.listdir(channel_dir) if os.path.isfile(os.path.join(channel_dir, f))]
    # Load each channel .json and grab the title
    self.channel_list = []
    for filename in filenames:
      # @todo Handle error
      with open(os.path.join(channel_dir, filename), 'r') as f:
        channel = json.load(f)
        self.channel_list.append(channel['name'])
        self.active_channel = channel['name']
        self.app.store.set('current_channel', snake(channel['name']))



  @on(Input.Submitted, '#chat-input')
  def on_chat_input(self, event):
    """
    - Add the prompt to the channel
    - Scroll to bottom
    - Clear the input
    - Persist message
    - Send the prompt to the API
    - Notify
    """
    message = {
      'role': 'user',
      'content': event.value,
      'timestamp': datetime.now().timestamp()
    }
    self.query_one('#chat-input').value = ''

    # Add the prompt to the channel
    new_message = Markdown(message['content'])
    messages = self.query_one('#chat-messages')
    messages.mount(new_message)

    # Scroll to bottom
    new_message.scroll_visible()

    # Persist message
    self.store.append('messages', message)

    # Notify
    self.notify(message['content'], title='Message persisted!')