import re
print(re.search(r'aza', 'plaza'))

print(re.search('aza', 'bazaar'))

print(re.search('aza', 'maze'))

print(re.search('^x', 'xenon'))

print(re.search('p.ng', 'penguin'))

print(re.search('p.ng', 'clapping'))

print(re.search('p.ng', 'pong'))

print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))


