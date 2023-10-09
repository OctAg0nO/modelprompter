import json
import os

class Store:
  def __init__(self, app, filename):
    self.app = app
    self.filename = os.path.join(os.path.abspath(__file__), os.path.abspath(filename))
    self.error = []
    self.data = self.load_data()

  def load_data(self):
    """
    - Loads the data from the file, if it exists.
    - If it doesn't, creates a new file, return an empty dict,
      and redirect to create a new connection
    """
    try:
      with open(self.filename, 'r') as f:
        return json.load(f)
    except FileNotFoundError:
      try:
        with open(self.filename, 'w') as f:
          json.dump({}, f)
          self.error.append(f'File not found, new one created: {self.filename}')
      except Exception as e:
        self.error.append(e)
      self.app.router.goto('connections')
      return {}

  def save_data(self):
    with open(self.filename, 'w') as f:
      json.dump(self.data, f)

  def get(self, key):
    return self.data.get(key)

  def set(self, key, value):
    self.data[key] = value
    self.save_data()