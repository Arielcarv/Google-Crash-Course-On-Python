# Event class - Date, Name, User, Type
# Login and Logout
# Attributes: Date, User, Machine, Type
# String receives list of event objects
# Machine Name: Users, separated by commas (,).
# PROBLEM
# We need to process a list of Event objects using their attributes to generate a report that lists all users currently logged in to the machines.

"""
numbers = [4, 6, 2, 7, 1]
numbers.sort()  # sort(key=[key for the sort comparison] , reverse= [If "True", sort the list reversed])
print(numbers)

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)
print(sorted(names))  # Return a new sorted list. Original keeps the same
print(names)

print(sorted(names, key=len))  # Sort by len of each string in the list

"""
"""
# EACH EVENT: Machine Name, User Name, Time, Login/Logout.


# Create a Class for the Events
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


# Helper function to sort the list
def get_event_date(event):
    return event.date


# Processing function
def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            if event.user in machines[event.machine]:
                machines[event.machine].remove(event.user)
    return machines


def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            users_list = ", ".join(users)
            print("{}: {}".format(machine, users_list))


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),]

users = current_users(events)
print(users)

print(generate_report(users))
"""
"""
for char in file_contents:
    if char not in punctuations:
        cleanstring += char


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be",
                           "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with",
                           "from", "here", "when",
                           "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor",
                           "too", "very",
                           "can", "will", "just"]

# Working LEARNER CODE 1
dictionary_of_frequencies = {}
file_contents2 = ""
    for letter in file_contents:
        if letter.isalpha():
           file_contents2 += letter.lower()
        else:
            file_contents2 += " "
    list_words = file_contents2.split()
    for word in list_words:
        if word not in uninteresting_words:
            if word in dictionary_of_frequencies:
                dictionary_of_frequencies[word] += 1
            else:
                dictionary_of_frequencies[word] = 1

# wordcloud
cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(dictionary_of_frequencies)
return cloud.to_array()

# Working LEARNER CODE 2

dictionary_of_frequencies = {}
file_contents2 = file_contents.split()

for word in file_contents2:
    if word not in uninteresting_words and punctuations:
        if word in dictionary_of_frequencies:
            dictionary_of_frequencies[word] += 1
        else:
            dictionary_of_frequencies[word] = 1


# Christina Sherin LEARNER CODE 2
dic = {}
    p = file_contents.split(" ")
    for word in p:
        wor=" "
        for c in word:
            if c not in punctuations:
                wor=wor+c
        if wor not in uninteresting_words:
            if wor not in dic.keys():
                dic[wor]=1
            else:
                dic[wor]+=1
    import wordcloud
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dic)
    return cloud.to_array()
"""  # Final Project


