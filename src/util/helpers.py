# Convert "strings with spaces" to "strings_with_underscores"
def snake(s):
  return '_'.join(word.lower() for word in s.split())