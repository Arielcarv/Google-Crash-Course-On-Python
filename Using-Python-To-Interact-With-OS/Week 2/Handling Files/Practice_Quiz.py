# import os

# def new_directory(directory, filename):
#   # Before creating a new directory, check to see if it already exists
#   if os.path.isdir(directory) == False:
#     os.mkdir(directory)

#   # Create the new file inside of the new directory
#   os.chdir(directory)
#   with open(filename):
#     pass

#   # Return the list of files in the new directory
#   os.chdir('../')
#   return os.listdir(directory)

# print(new_directory("PythonPrograms", "script.py"))


# import os
# import datetime

# def file_date(filename):
#   # Create the file in the current directory
#   open(filename, 'w').close()
#   timestamp = os.path.getmtime(filename)
#   # Convert the timestamp into a readable format, then into a string
#   formated_date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
#   # Return just the date portion 
#   # Hint: how many characters are in “yyyy-mm-dd”? 
#   return ("{}".format(formated_date))

# print(file_date("newfile.txt")) 
# # Should be today's date in the format of yyyy-mm-dd



# import os
# def parent_directory():
#   # Create a relative path to the parent 
#   # of the current working directory 
#   current_directory = os.getcwd()
#   above_directory_name = current_directory.split(os.sep)[-2]
#   os.chdir('../../')
#   relative_parent = os.path.join(os.getcwd(), above_directory_name)

#   # Return the absolute path of the parent directory
#   return relative_parent

# print(parent_directory())

import os

def parent_directory():

  # Create a relative path to the parent 

  # of the current working directory 

  relative_parent = os.path.join(os.getcwd(),'..')

  # Return the absolute path of the parent directory

  return os.path.abspath(relative_parent) # The abspath normalizes the '..' in the end indicating it has to come back one directory.

print(parent_directory())