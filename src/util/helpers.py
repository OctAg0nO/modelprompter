# Convert "strings with spaces" to "strings_with_underscores"
def snake(s):
  return '_'.join(word.lower() for word in s.split())

# Convert "strings_with_underscores" to "strings with underscores"
def desnake(s):
  return ' '.join(word for word in s.split('_'))