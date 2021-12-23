print("")

'''
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.")
    else:
        print("Valid username.")
'''

''' 
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long.")
        else:
            print("Valid username.")
'''

'''
hint_username("Jo")
hint_username("Jonas")
hint_username("Jonasabacaximoreira")

print("")

def is_even(number):
    if number % 2 == 0:
        return True
    return False


print(is_even(4))
print(is_even(5))
print(is_even(6))
'''

''' 
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = (filesize // block_size)
    print(full_blocks)
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = (filesize % block_size)
    print(partial_block_remainder)
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (4096*(full_blocks+1))
    return (4096*full_blocks)

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
'''

'''
def format_name(first_name, last_name):
    # code goes here
    if first_name != "" and last_name != "":
        string = "Name: " + last_name +", "+ first_name
    elif first_name == "" and last_name == "":
        string = ""
    elif first_name == "" and last_name != "":
        string = "Name: " + last_name
    else:
        string = "Name: " + first_name
    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
'''

print((10 >= 5*2) and (10 <= 5*2))
print("big" > "small")
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
	# keep just the fractional part of the quotient
	if denominator == 0 or numerator == 0:
		return 0
	elif numerator >= denominator:
		return (numerator % denominator)/denominator


print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0