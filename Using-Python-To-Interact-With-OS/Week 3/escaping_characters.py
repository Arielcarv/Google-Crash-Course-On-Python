import re

print(re.search(r'.com', 'welcome'))

print(re.search(r'\.com', 'welcome'))

print(re.search(r'\.com', 'mydomain.com'))

# \d (Match digits)
# \w (Match letters, numbers and underscores)
# \s (Match whitespace, tabs and new lines)

print(re.search(r'\w*', 'This is an example'))

print(re.search(r'\w*', 'And_this_is_another'))

print(re.search(r'\w+\s+\w+', '123  Ready Set GO'))

print(re.search(r'\w+\s+\w+', 'shopping_list: milk, bread, eggs.'))
