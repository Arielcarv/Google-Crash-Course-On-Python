import re

print(re.search(r'Py.*n', 'Pymalion'))

print(re.search(r'Py.*n', 'Python Programming'))

print(re.search(r'Py[a-z]*n', 'Python Programming'))

# Repetition qualifiers '+'(one or more) & '?'(only one)
print(re.search(r'o+l+', 'goldfish'))

print(re.search(r'o+l+', 'woolly'))

print(re.search(r'o+l+', 'boil'))

print(re.search(r"p?each","To each their own"))

print(re.search(r"p?each","i like peaches"))
