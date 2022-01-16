import re

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result.group())
print(result.end())
print(f'''Index 0: {result[0]} .
Index 1: {result[1]} .
Index 2: {result[2]} .''')

def rearrange_name(name):
    result = re.search(r"^(\w*), ((\w*)|.*\.)$", name)
    # result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return f"{result[2]} {result[1]}"

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))
print(rearrange_name("Kennedy, John F."))
