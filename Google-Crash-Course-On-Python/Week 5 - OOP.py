# Object Oriented Programming
# A flexible, powerful paradigm where classes represent and define concepts,
# while objects (Numbers, Strings, Lists, Dict.) are instances of classes

# ATTRIBUTE . Characteristics associated to a type.
# METHODS . Functions associated to a type (specific instance of a class).

"""
print(type(0))
print(type(""))

print(dir(""))  # Print all the attributes of a class

print(help(int))  # Print all the documentation of the class



# Write our own classes
class Apple:
    pass


class Apple:
    color = ""
    flavor = ""

# jonagold is an instance of the apple class.
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())

# golden is another instance of the apple class.
golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"
print(golden.color)
print(golden.flavor)
"""  # Object Oriented Programming
"""
# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Here, despite G.B. Shaw's quote, our characters have started with
    # different amounts of apples so we can better observe the results.
    # We're going to have Martin and Johanna exchange ALL their apples with #one another.
    # Hint: how would you switch values of variables,
    # so that "you" and "me" will exchange ALL their apples with one another?
    # Do you need a temporary variable to store one of the values?
    # You may need more than one line of code to do that, which is OK.
    quantity_me = you.apples
    quantity_you = me.apples
    you.apples = quantity_you
    me.apples = quantity_me

    return you.apples, me.apples


def exchange_ideas(you, me):
    # "you" and "me" will share our ideas with one another.
    # What operations need to be performed, so that each object receives
    # the shared number of ideas?
    # Hint: how would you assign the total number of ideas to
    # each idea attribute? Do you need a temporary variable to store
    # the sum of ideas, or can you find another way?
    # Use as many lines of code as you need here.
    you.ideas += me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))
"""  # Question 2 # Practice Quiz: Object Oriented Programming
"""
# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if (city1.population >= min_population) and (city1.elevation > return_city.elevation):
        return_city = city1
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if (city2.population >= min_population) and (city2.elevation > return_city.elevation):
        return_city = city2
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if (city3.population >= min_population) and (city3.population < return_city.elevation):
        return_city = city3

    # Format the return string
    if return_city.name:
        return f"{return_city.name}, {return_city.country}"
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""

"""  # Question 3
"""
class Furniture:
    color = ""
    material = ""


table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"


def describe_furniture(piece):
    return "This piece of furniture is made of {} {}".format(piece.color, piece.material)


print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"
"""  # Question 5

# Classes and Methods

"""
class Piglet:
    '''Represents a piglet that can say their name'''
    name = "piglet"
    years = 0

    def speak(self):
        '''Outputs a message inlcuding the name of the piglet.'''
        print(f"Oink! I'm {self.name}! Oink!")

    def pigyears(self):
        '''Converts teh current age to equivalent pig years.'''
        return self.years * 18


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

piggy = Piglet()
print(piggy.pigyears())

piggy.years = 2
print(piggy.pigyears())

help(Piglet)
help(Piglet.speak)
help(Piglet.pigyears)


"""  # Instance Methods
"""class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):  # What to display when the print function is called.
        return f"This apple is {self.color} and its flavor is {self.flavor}"


jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold.flavor)


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return f"hi, my name is {self.name}"

    # Create a new instance with a name of your choice


some_person = Person("Rogerin do Querô")
# Call the greeting method
print(some_person.greeting())

print(jonagold) # Default representation. Place of the object in the computer's memory.
"""  # Constructor. The method that's called when you call the name of the class. [__init__]
"""
def to_seconds(hours, minutes, seconds):
    '''Returns the amount of seconds in the given hours, minutes and seconds'''
    return hours * 3600 + minutes * 60 + seconds


help(to_seconds)
"""  # Documenting Functions. Doc Strings - To help others to understand the code you've written
"""class Fruit:
    '''Mother class of all fruits'''
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


class Apple(Fruit):
    pass


class Grape(Fruit):
    pass


granny_smith = Apple("Green", "tart")
carnelian = Grape("purple","sweet")
print(granny_smith.flavor)
print(granny_smith.color)
print(carnelian.flavor)
print(carnelian.color)

class Animal:
    sound = ""
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.sound} I'm {self.name}! {self.sound}")

class Piglet(Animal):
    sound = "Oink!"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "Mooooo"

milky = Cow("Milky White")
milky.speak()

class Clothing:
    material = ""
    def __init__(self, name):
        self.name = name
    def checkmaterial(self):
        print(f"This {self.name} is made of {self.material}")

class Shirt(Clothing):
    material = "Cotton"

polo = Shirt("Polo")
polo.checkmaterial()"""  # Inheritance
"""
class Repository:
    def __init__(self):
        self.packages = {} # Always initialize mutable attributes in the constructor.
    def add_package(self,package):
        self.packages[package.name] = package
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(name)
        Clothing.stock['material'].append(material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = 'Cotton'


class pants(Clothing):
    material = 'Cotton'


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)"""  # Composition
"""import random

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))


import datetime
now = datetime.datetime.now()
print(now)
print(type(now))
print(now.year)
print(now + datetime.timedelta(days=28)) # Add 28 days to the current date (now)."""  # Python Modules - Used to organize functions, classes and other data together in a structured way
"""class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


class Turtle(Animal):
    name = "Michelangelo"
    category = "reptile"


#Turtle = Turtle("Michelangelo")
#Turtle.set_category("reptile")
print(Turtle.name)
print(Turtle.category)


class Snake(Animal):
    name = "Naja"
    category = Turtle.category


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


zoo = Zoo()


turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category"""  # Code Reuse Lab

# Begin Portion 1#
import random


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random() * 10 + 1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]
    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())


# End Portion 1#


server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())


# Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        for connection in self.connections.keys():
            if connection == connection_id:
                corresp_server = self.connections[connection]

            # Close the connection on the server
            corresp_server.close_connection(connection_id)
        # Remove the connection from the load balancer
        del self.connections[connection_id]

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        numb_servers = 0
        for server in self.servers:
            total_load += server.load()
            numb_servers += 1
        return total_load/numb_servers

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() >= 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))


# End Portion 2#


l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())
