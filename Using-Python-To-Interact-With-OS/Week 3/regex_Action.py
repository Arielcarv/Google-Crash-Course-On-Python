import re

print(re.search(r'^A.*a$', 'Argentina'))
print(re.search(r'^A.*a$', 'Azerbaijan'))

pattern = r'^[a-zA-Z_][\w]*$'

print(re.search(pattern, '_this_is_a_valid_variable_name'))
print(re.search(pattern, "this isn't a valid varible"))
print(re.search(pattern, 'my_variable1'))
print(re.search(pattern, '2my_variable1'))

print(re.search(r"^[A-Z]+[\w\s]*[\.!\?]+$","Is this is a sentence?"))
print(re.search(r"^[A-Z]+[\w\s]*[\.!\?]+$","is this is a sentence?"))
print(re.search(r"^[A-Z]+[\w\s]*[\.!\?]+$","Hello"))