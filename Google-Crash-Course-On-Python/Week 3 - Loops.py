###### WHILE LOOPS #######

"""
x = 0
while x < 5:
    print("Not There Yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


def attempts (n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x+=1
    print("Done")
attempts(5)


my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1

x = 1
sum = 0
while x < 10:
    sum += x
    x += 1

product = 1
while x < 10:
    product = product * 1
    x += 1

print(sum, product)
"""  # CLASSES

"""  
def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0 and n != 0:
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

# MY WAY
def sum_divisors(n):
    sum = 0
    soma = 0
    counter = 1
    # Return the sum of all divisors of n, not including n
    while counter < n:
        if (n % counter) == 0:
            if (n // counter) == n:
                soma += counter
            else:
                soma += (n // counter)
        counter += 1
    sum = soma
    return sum

print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114


# INTERNET WAY
def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(8))
print(sum_div(12))


def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
        # What is the additional condition to exit out of the loop?
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result), end = ' ')
        # Increment the variable for the loop
        multiplier += 1
    print('')


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24
"""  # PRACTICE QUIZ - While Loops

####### FOR LOOPS ########
'''
def square(n):
    return n*n
def sum_squares(x):
    sum = 0
    n = 0
    for n in range (x): # n goes from 0 to 10 - ((1²)+2²)+3³...
        sum += square(n)
        print(sum)
    return sum
print(sum_squares(10)) # Should be 285

friends = ['Kleber', 'Paulo', 'Estevam', 'Valtim']
for friend in friends:
    print("Hi", friend)


values = [25,35,76,98,50]
sum = 0
length = 0
for value in values:
    sum += value
    length+=1
print("Total sum: "+ str(sum) + " - Average: " + str(sum/length))

product = 1
for n in range(1,10):
    product = product * n
print(product)

### FACTORIAL ###
def factorial(n):
    result = 1
    for i in range (n):
        result = result * i
    return result
print(factorial(4))
print(factorial(5))

### CELSIUS CONVERSION ###
def to_celsius(x):
    return (x-32)*5/9
for x in range (0,101,10): #Goes from [0 to 100] in steps of [10]
    print(x, to_celsius(x))

# NESTED 'FOR' LOOPS
for left in range(7): # 0 to 6 on the left side.
    for right in range (left, 7): # Nº on the left and nº on the right from [nº left to 6]
        print("["+ str(left)+ "|" + str(right) + "]", end=" ")
    print()

# TEAMS
teams = ['Goyta', 'Lamparões', 'Curizcus', 'Cabalos']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# MISTAKES
def is_valid(user):
    if len(user) >= 3:
        return True
    else:
        return False

def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")

validate_users(["purplecat"])
'''  # CLASSES

'''
def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result
for n in range(0,10):
    print(n, factorial(n+1))

for cube in range(1,11):
  print(cube**3)

for multiples_of_seven in range(0, 100, 7):
    print(multiples_of_seven)


def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
            break
        else:
            print("Attempt " + str(n) + " failed")
retry(create_user, 3)
retry(stop_service, 5)
'''  # PRACTICE QUIZ - FOR LOOPS

####### RECURSION ########
'''
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


print(factorial(5))

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
'''  # CLASSES

'''
def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1 and base != 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number/base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False



def sum_positive_numbers(n):
    if n > 0:
        total = n + sum_positive_numbers(n - 1)
        return total
    else:
        return 0

print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15
'''  # PRACTICE QUIZ - RECURSION

'''
number = 1
while number <= 7:
    print(number, end=" ")
    number += 1



def show_letters(word):
    for letter in range(0, len(word), 1):
        print(word[letter])


show_letters("Hello") # Should print one line per letter


def digits(n):
    count = 0
    if n == 0:
        return 1
    while n >= 1:
        count += 1
        n = n / 10
    return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1


def multiplication_table(start, stop):
    for x in range(start, stop+1):
        for y in range(start, stop+1):
            print(str(x * y), end=" ")
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above


def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x += 1
    return return_string


print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1))  # Should be "Counting down: 2,1"
print(counter(5, 5))  # Should be "Counting up: 5"


def even_numbers(maximum):
    return_string = ""
    for x in range(2, (maximum + 1), 2):
        return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10))  # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


for x in range(1, 10, 3):
    print(x)

for x in range(10):
    for y in range(x):
        print(y)


def decade_counter():
    year = 0
    while year < 50:
        year += 10
    return year

print(decade_counter())


'''  # MODULE 3 - GRADED ASSESSMENT
