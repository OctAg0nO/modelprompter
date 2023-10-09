import json
from textual.reactive import reactive

class Store:
  def __init__(self, app, filename: str):
    self.app = app
    self.filename = filename
    self.error = reactive([])
    self.data = reactive(self.load_data())

  def load_data(self) -> dict:
    try:
      with open(self.filename, 'r') as f:
        return json.load(f)
    except FileNotFoundError:
      self.error.appen[f'File not found, new one created: {self.filename}']
      try:
        with open(self.filename, 'w') as f:
          json.dump({}, f)
      except Exception as e:
        self.error.append(e)
      return {}

  def save_data(self):
    with open(self.filename, 'w') as f:
      json.dump(self.data, f)

  def get(self, key):
    return self.data.get(key)

  def set(self, key, value):
    self.data[key] = value
    self.save_data()