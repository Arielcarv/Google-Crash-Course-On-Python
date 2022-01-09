# with open('spyder.txt') as file:
#     for line in file:
#         print(line.upper().strip()) 

# file = open('spyder.txt')
# lines = file.readlines()
# file.close()
# print(lines)
# lines.sort()
# print(lines)

## Write in file
# "r" -> Read
# "w" -> Write
# "a" -> Append
# "r+" -> Read+write
with open('novel.txt', 'w') as novel:
    novel.write("It was a dark and stormy night\n")


with open('novel.txt', 'a') as novel:
    novel.write("It was a dark and stormy night2")