import os
import json
from textual.reactive import reactive
from textual.widgets import Button, Static, Placeholder, Input, Label, Markdown
from textual.containers import ScrollableContainer, Horizontal, Vertical

class Chat(Static):
  BINDINGS = []
  app = {}
  channel_list = reactive(list(), always_update=True, init=False)



  def __init__(self, app, id):
    super().__init__()
    self.app = app
    self.id = id
    self.load_channels()



  def compose(self):
    with Horizontal():
      with ScrollableContainer(id='chat-sidebar', classes='sidebar mt0'):
        yield Markdown('## Channels')
        for channel in self.channel_list:
          yield Label(str(channel))
      with Vertical(classes='pl1'):
        with ScrollableContainer():
          yield Placeholder('Messages')
        with Horizontal(id='chat-input-wrap', classes='p0'):
          yield Input(value='', id='chat-input', placeholder='Type your prompt here...')



  def on_mount(self):
    """
    - Focus input
    - Create default channel/message if not exist
    - Load existing channels/messages
      - Select the active channel
    """
    self.query_one('#chat-input').focus()



  def load_channels(self):
    self.maybe_create_default_channel()
    channel_dir = os.path.join(os.getcwd(), 'data', 'chat')
    # Load all filenames in data/chat into an array
    filenames = [f for f in os.listdir(channel_dir) if os.path.isfile(os.path.join(channel_dir, f))]
    # Load each channel .json and grab the title
    self.channel_list = []
    for filename in filenames:
      with open(os.path.join(channel_dir, filename), 'r') as f:
        channel = json.load(f)
        self.channel_list.append(channel['name'])



  def maybe_create_default_channel(self):
    """
    - Each channel is a .json file in the /data/chat directory
    """
    # Create /data/chat/general.json if it doesn't exist
    channel_dir = os.path.join(os.getcwd(), 'data', 'chat')
    if not os.path.exists(channel_dir):
      os.makedirs(channel_dir)
    channel_path = os.path.join(channel_dir, 'general.json')
    if not os.path.exists(channel_path):
      with open(channel_path, 'w') as f:
        default_channel = {'name': 'General', 'messages': []}
        json.dump(default_channel, f)
