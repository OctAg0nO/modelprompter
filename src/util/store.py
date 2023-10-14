import json
import os
from util.helpers import snake

class Store:
  def __init__(self, app, filename, default={}):
    self.app = app
    self.filename = snake(os.path.join(os.path.abspath(__file__), os.path.abspath(filename)))
    self.error = []
    self.data = self.load_data(default)

  def load_data(self, default={}):
    """
    - Loads the data from the file, if it exists.
    - If it doesn't, creates a new file, return an empty dict,
      and redirect to create a new connection
    """
    try:
      with open(self.filename, 'r') as f:
        return json.load(f) or default
    except FileNotFoundError:
      try:
        with open(self.filename, 'w') as f:
          json.dump(default, f)
          self.app.print(f'🚨 File not found, new one created: {self.filename}')
      except Exception as e:
        self.app.print(f'🚨 {e}')
      return default



  def save_data(self):
    with open(self.filename, 'w') as f:
      json.dump(self.data, f, indent='\t')



  def get(self, key, default=None):
    return self.data.get(key, default)



  def set(self, key, value):
    self.data[key] = value
    self.save_data()



  def append(self, key, value):
    if (not self.data.get(key)):
      self.data[key] = []
    self.data[key].append(value)
    self.save_data()