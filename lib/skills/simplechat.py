import openai

def run(connection, messages):
  # Setup API
  openai.api_type = connection.get('api_type', 'open_ai')
  openai.api_key = connection.get('key', 'OPENAI_API_KEY')
  openai.api_base = connection.get('api_base', 'https://api.openai.com/v1')
  openai.api_version = connection.get('api_version', None)
  model = connection.get('model', 'gpt-3.5-turbo-16k')

  # Make a clone of the messages with only .role and .content
  messages = list(map(lambda message: {
    'role': message['role'],
    'content': message['content']
  }, messages))

  # Create a chat completion
  return openai.ChatCompletion.create(model=model, messages=messages)

