import re

print(re.search(r'[Pp]ython', 'python'))

print(re.search(r'[a-z]way', 'The end of the highway.'))

print(re.search(r'[a-z]way', 'What a way to go.'))

print(re.search(r'cloud[a-zA-Z0-9]', 'cloudy9'))

print(re.search(r'[.!?]', 'This is a sentence that ends with a period'))

# Negative '^', don't match what is specified.
print(re.search(r'[^a-zA-Z]', 'This is a sentence with spaces.'))

print(re.search(r'[^a-zA-Z ]', 'This is a sentence with spaces.'))

# OR operator
print(re.search(r'cat|dog', 'I like cats.'))

print(re.search(r'cat|dog', 'I like dogs.'))

print(re.search(r'cat|dog', 'I like both dogs and cats.'))

# Find all matches
print(re.findall(r'cat|dog', 'I like both dogs and cats.'))