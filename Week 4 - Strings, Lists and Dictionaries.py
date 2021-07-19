###### STRINGS #######

'''name = "Sasha"
color = 'Gold'
place = "Cambridge"

pet = ""
pet = "loooooooooooooooooong cat"
print("Name: " + name + ", Favorite color: " + color)

print("example " * 3)

len(pet)


def double_word(word):
    return (word * 2) + str(len(word * 2))


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))  # Should return abcabc6
print(double_word(""))  # Should return 0

## Print last character of string
text = "Random string with a lot of characters"
print (text[-1])

def first_and_last(message):
    if (message == '') or (message[0] == message[-1]):
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

## Slice
color = "Orange"
color[1:4]

fruit = "Pineapple"
fruit [:4]
fruit [4:]


message1 = "A kong string with a silly typo"
#message[2] = "l"    Strings in Python are immutable.

new_message = (message1[0:2] + "l" + message1[3:])
print(new_message)

pets = "Cats & Dogs"
pets.index("&")
#"Dragons" in pets  #Check if contains the fragment


def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index]+ "@" + new_domain
        return new_email
    return email


print(replace_domain("arilius@abacate.com","abacate.com","café.com"))


## String Methods ##
name.upper() #All characters become 'UPPERCASE'
name.lower() #All characters become 'lowercase'
" yes ".strip() #Strip spaces from edges
text.count("e") #Count the number of characters
text.endswith("ers") #Test if the string ends with the fragment explicited
text.isnumeric() #Test if the string is a numeric, if it's numeric we can use the "INT" function
" ".join(["This","is", "a","phrase","joined","by","spaces"])
"...".join(["This","is", "a","phrase","joined","by","triple","dots"])
"This is another example".split()
text.replace("a", "abacate") #string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS

## FORMAT String Methods ##

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}.".format(name, number))
print("Hello {name}, your lucky number is {number}.".format(name=name, number=number))


def student_grade(name, grade):

    return "{name} receive {grade}% on the exam".format(name=name, grade=grade)

########## EXAMPLES
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

name = "Micah"
print(f'Hello {name}') #Hello Micah

item = "Purple Cup"
amount = 5
price = amount * 3.25
print(f'Item: {item} - Amount: {amount} - Price:{price:.2f}.')


# Formatting expression "[ :.2f ]" . Formatting a float number with two digits after the dot(.)
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print(f"The price is ${price}, but with taxes is ${with_tax:.2f}")


def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print(x, to_celsius(x))
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
#{:>3} - Number aligned to the right with total of 3 spaces
#{:>6.2f} - Number aligned to the right with total of 6 spaces and to show 2 decimal numbers.
'''  # CLASSES

'''
Weather = "Rainfall"
print(Weather[:4])



def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    print()
    # Traverse through each letter of the input string
    for letter in input_string.lower():
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        print(letter, end="")
        if letter != " ":
            new_string = new_string + letter
            reverse_string = letter + reverse_string
    # Compare the strings
    if new_string == reverse_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


def convert_distance(miles):
    km = miles * 1.6
    result = f'{miles} miles equals {km:.1f} km'
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km


def nametag(first_name, last_name):
    return "{first_name} {last_name}.".format(first_name=first_name, last_name=last_name[0])


print(nametag("Jane", "Smith")) # Should display "Jane S."
print(nametag("Francesco", "Rinaldi")) # Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre")) # Should display "Jean-Luc G."


def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = len(old)
        new_sentence = sentence[:-i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
'''  # PRACTICE QUIZ - STRINGS

####### LISTS ########
# CLASSES
'''
x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(x)
print(len(x))

# Check if the element is into the list
print("are" in x)
print("Today" in x)

word = 0
while word < 4:
    print(x[word], end=" ")
    word += 1

# Return the element in the index n specified
def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        #print(words)
        #print(len(words))
        if n <= len(words):
            return words[n-1]
    return ""


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing
'''  # Lists Defined
'''
# ( .append ) # ADD something to the end of a list
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
print(f'String: fruits{fruits}')
fruits.append("Kiwi")
print(f'String: fruits.append("Kiwi"): {fruits}')

# ( .insert(index, new_element) ) # Insert an element in the middle of the list
fruits.insert(0, "Orange")
print(f'String: fruits.insert(0, "Orange"): {fruits}')
# If you use an index greater than the list the element is added to the end [No Error]
fruits.insert(25, "Peach")
print(f'String: fruits.insert(25, "Peach"): {fruits}')

# ( .remove ) #Remove The fist occurrence of the specified element from the list
fruits.remove("Melon")
print(f'String: fruits.remove("Melon"): {fruits}')

# ( .pop(index) ) #Return the REMOVED element from the index
print(fruits.pop(3))
print(f'String: fruits.pop(3): {fruits}')

# Assign something else in the list
fruits[3] = "Strawberry"
print(f'String: fruits[3] = "Strawberry": {fruits}')
'''  # Modifying contents of a Lists
'''
# Skip every other(odd indexes) element from list
def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if (i % 2) == 0:
            # Add this element to the resulting list
            new_list.append(elements[i])
        # Increment i
        i += 1
    return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([]))  # Should be []
'''  # Modifying Lists
'''
fullname = ('Grace', 'M', 'Hopper')


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
print(result)
print(type(result))

# Unpacking Tuples - Turn 3 elements to 3 separate variables
hours, minutes, remaining_seconds = result
print(hours, minutes, remaining_seconds, "\n")
hours, minutes, remaining_seconds = convert_seconds(1000)
print(hours, minutes, remaining_seconds)


def file_size(file_info):
    name, type, size = file_info
    return "{:.2f}".format(size / 1024)


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21
'''  # Lists and Tuples(Sequence of immutable elements of any type)
'''
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print(f'Total characters: {chars}, Average length: {chars / len(animals)}')

# enumerate (iterable, start = 0) - Assign an index to each item in the list, tuple or string
# In case of "for" use teh first element is the index and the second the element itself.  
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print(f'{index + 1} - {person}')


def skip_elements(elements):
    # code goes here
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)
    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']


def full_emails(people):
    result = []
    for email, name in people:
        result.append(f'{name}, <{email}>')
    return result


print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
'''  # Interacting over Lists and Tuples
'''
# Create a list of multiples of 7
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

multiples = [x*7 for x in range(1, 11)]
print(multiples)


languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

# Multiples of 3 by list
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

# Return a list o Odd numbers between 1-n
def odd_numbers(n):
    return [x for x in range(0,n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
'''  # List Comprehensions
'''
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
#for x in filenames:
#  new = (x, x.replace(".hpp", ".h"))
#  newfilenames.append(new)
for element in filenames:
    if element[-2:] == 'pp' or element.endswith('pp'):
        newfilenames.append(element[:-2])
    else:
        newfilenames.append(element)
print(newfilenames) # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    print(words)
    for word in words:
        # Create the pig latin word and add it to the list
        lword = word[0]
        say += word[1:] + lword + "ay "
        #print(say)
        # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for octal_digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if octal_digit >= value:
                result += letter
                octal_digit -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

## Question 5

def group_list(group, users):
    members = ", ".join(users)
    return f'{group}: {members}'


def group_list(group, users):

if users == "":

return "{}:{}".format(group,"")

for user in users:

member = " ,".join(users)

return "{}:{}".format(group, member)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"


## Question 6

def guest_list(guests):
    for guest in guests:
        name, age, profession = guest
        print("{name} is {age} years old and work as {profession}".format(name=name, age=age, profession=profession))
        print(f'{name} is {age} years old and work as {profession}')

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
'''  # PRACTICE QUIZ - LISTS

####### DICTIONARIES ########
'''
#(The data inside dictionaries take the form od pairs of keys and values.) MUTABLE

# {key: value}

x = {}
print(type(x))

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts,"\n")

# Return the value inside the key
print(file_counts["txt"])

# Check if dictionary contains
print("jpg" in file_counts)
print("html" in file_counts,"\n")

# Adding key to dictionary
file_counts["cfg"] = 8
print(file_counts, "\n")

# If Add one key the already exists (The value is REPLACED)
file_counts["csv"] = 17
print(file_counts, "\n")

# DELETE files from dictionary
del file_counts["cfg"]
print(file_counts)


toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}

toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?
'''  # Dictionaries
'''
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)

# Iterating each Item of the dictionary
for ext, amount in file_counts.items():
    print(f"There are {amount} files with the .{ext} extension")

# Show Keys in a dictionary
print(file_counts.keys())

# Show Values of each key in a dictionary
print(file_counts.values())
for value in file_counts.values():
    print(value, end=' ')

# Example
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast, limb in cool_beasts.items():
    print("{beast} have {limb}".format(beast=beast, limb=limb))

# Counting how many times each letter appear in a piece of text
def count_letters(text):
    result = {} # Initialize empty dictionary
    for letter in text:  # Goes to each letter
        if letter not in result: # For each letter, check if it's not in the dictionary
            result[letter] = 0 # If not, initialize 0
        result[letter] += 1 #IF there is the letter, add 1
    return result

print(count_letters("aaaaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))
'''  # Iterating over the contents of a dictionary
'''
## List:
# If you've got a list of information you'd like to collect. Ex: A serie of IP address to PIN
ip_addresses = ["192.168.1.1", "127.0.0.1", "8.8.8.8"]
# Can store any data type

## Dictionary
# A list of host name and corresponding IP Addresses.
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}

# Use Dictionary when searching for a specific element
# Can store any data type for values, but keys are immutable types(numbers,booleans,strings,tuples)(NOT lists or dictionaries).

wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for piece, color in wardrobe.items():
    for each_color in color:
        #print("{} {}".format(each_color, piece))
        print(f'{each_color} {piece}')
'''  # Dictionaries vs. Lists # SET [IMMUTABLE] = Used to store a bunch of elemens and be certain they're only present once
'''
# Question 1
def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user+"@"+domain)
    return (emails)


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]}))


# Question 2

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user not in user_groups:
                user_groups[user] = [] #Add Key "user" to dictionary with value =0
            user_groups[user].append(group)
    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))


# Question 5
def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for item, value in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += value
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44
'''  # PRACTICE QUIZ - Dictionaries


'''
# Question 1
def format_address(address_string):
    # Declare variables
    house_number = ""
    street_name = ""
    # Separate the address string into parts
    address_list = address_string.split()
    # Traverse through the address parts
    #print(address_list)
    for element in address_list:
        # Determine if the address part is the
        # house number or part of the street name
        if element.isnumeric():
            house_number = element
        else:
            #print(element)
            street_name += element + " "


    # Does anything else need to be done
    # before returning the result?
    #street_name.lstrip()
    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


# Question 2

def highlight_word(sentence, word):
    return sentence[:sentence.index(word)] + word.upper() + sentence[sentence.index(word)+len(word):]


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


# Question 3

def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order

    complete_list = list2 + list1[::-1]
    return complete_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


# Question 4

def squares(start, end):
    return [n * n for n in range(start, end + 1, 1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Question 5

def car_listing(car_prices):
    result = ""
    for car, price in car_prices.items():
        result += "{} costs {} dollars".format(car, price) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000, "Ford Fiesta": 13000, "Toyota Prius": 24000}))



# Question 6

def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    final_guestlist = {}
    final_guestlist.update(guests2)
    final_guestlist.update(guests1)
    return final_guestlist


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1, "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1, "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Question 7


def count_letters(text):
  result = {}
  text = text.replace(" ","")
  # Go through each letter in the text
  for letter in text.lower():
    # Check if the letter needs to be counted or not
    if letter.isalpha():
        if letter not in result:
            result[letter] = 0
        # Add or increment the value in the dictionary
        result[letter] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])
'''  # MODULE 4 - GRADED ASSESSMENT
