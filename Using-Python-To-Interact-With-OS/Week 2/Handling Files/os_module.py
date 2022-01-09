import os

def create_file(name, text):
    return open(name, 'w').write(text)


# Delete a file
if os.path.exists('new_novel.txt'):
    os.remove('new_novel.txt')
else:
    create_file('new_novel', 'Just the same old story!')
    os.remove('new_novel.txt')

create_file('new_novel', 'Just the same old story!')

# Rename filenames -> rename('OLDNAME', 'NEWNAME')
print(os.rename('novel.txt', 'newnovel.txt'))

# Check if the file exists
print(os.path.exists('novel.txt')) # Returns true if the directory or file exists.
print(os.path.isfile('novel.txt')) # Returns true ONLY the file exists.

# Check size of a filenames
print(os.path.getsize('spyder.txt'))

# Check modification time in UNIX timestamp format(seconds since january, 1970)
print(os.path.getmtime('spyder.txt'))

# Find out the absolute system path for the file.
print(os.path.abspath('spyder.txt'))

######       WORKING WITH DIRECTORIES    #########
# Find out Current working directory
print(os.getcwd())

# Make a new directory
os.mkdir('new_dir')

# Change the current working directory
os.chdir('/home/')

# Delete EMPTY directory
os.rmdir('new_dir')

# List of all files in subdirectories and current directory.
os.mkdir('website')
os.chdir('website')
os.mkdir('images')
create_file('index.html', '<h1>nothing here too</h1>')
create_file('favicon.ico', 'avocado')
os.chdir('./../')
os.listdir('website')

# Find out if it is a directory of file.
directory = 'website'
for name in os.listdir(directory):
    fullname = os.path.join(directory, name)
    if os.path.isdir(fullname):
        print(f'{fullname} is a directory.')
    else:
        print(f'{fullname} is a file.')
