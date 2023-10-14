import os
import json
from datetime import datetime
import importlib
import sys

from util.store import Store
from util.helpers import snake

from textual import on
from textual.reactive import reactive
from textual.widgets import Static, Input, DataTable, Markdown
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
      'script': 'lib.skills.simplechat'
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

    self.load_initial_messages()



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
    """
    message = {
      'role': 'user',
      'content': event.value,
      'timestamp': datetime.now().timestamp()
    }
    self.query_one('#chat-input').value = ''

    # Add the prompt to the channel
    new_message = Markdown(message['content'], classes=f'chat-message chat-message-role-{message["role"]}')
    messages = self.query_one('#chat-messages')
    messages.mount(new_message)

    # Scroll to bottom
    new_message.scroll_visible()

    # Persist message
    self.store.append('messages', message)
    
    # Send prompts to API
    module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', self.store.get('script')))
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    sys.path.insert(0, os.path.dirname(module_path))

    # Use importlib to import the module dynamically
    module = importlib.import_module(module_name)

    connections = self.app.store.get('connections')
    current_connection = self.app.store.get('current_connection')
    current_connection = list(filter(lambda connection: connection['id'] == current_connection, connections))[0]
    response = module.run(current_connection, self.store.get('messages'))

    # @todo lets store the full data
    # Add the response message to the channel
    if (response):
      # Report empty
      if (not response):
        response = {
          'role': 'error',
          'content': 'No response',
          'timestamp': datetime.now().timestamp()
        }
      # Report errors
      elif (response.get('error')):
        response = {
          'role': 'error',
          'content': response.get('error'),
          'timestamp': datetime.now().timestamp()
        }
      # Report success
      else:
        response = {
          'role': 'assistant',
          'content': response['choices'][0]['message']['content'],
          'timestamp': datetime.now().timestamp()
        }

      new_message = Markdown(response['content'], classes=f'chat-message chat-message-role-{response["role"]}')
      self.store.append('messages', response)
      messages.mount(new_message)
      new_message.scroll_visible()



  def load_initial_messages(self):
    messages = self.query_one('#chat-messages')
    last_message = None
    for message in self.store.get('messages'):
      last_message = Markdown(message['content'], classes=f'chat-message chat-message-role-{message["role"]}')
      messages.mount(last_message)

    # Scroll to bottom
    if (last_message):
      last_message.scroll_visible()