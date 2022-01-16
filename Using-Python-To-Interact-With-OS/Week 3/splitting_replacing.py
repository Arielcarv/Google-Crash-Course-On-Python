import re 

print(re.split(r"[.?!]", "One Sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One Sentence. Another one? And the last one!"))

print(re.sub(r"[\w.%+-]+@[\w+-]+", "[SUBSTITUTED_PART]","Received an email for go_nuts95@my.example.com"))

# Capture group 1 = \1. 
# Capture group 2 = \2.
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")) 

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))