import json

# this is a relative path to the .json data file
# you can also use a 'full' or 'absolute path' to the file
# windows and mac paths are different.  You should google and youttube to learn about paths if you are
# not familiar with them.  They are important fundamental computer concepts.
#
# this is a full windows path, note the forward slashes '/' used in python
# pathToFile = 'E:/Users/jerome/GitHub/evc-cit134a-python/birthday/birthday.json'
#
# mac (which is built on linux) and linux paths are like this: 'a/b/c/d/e/f.json'
#

# relative path
# pathToFile = './birthday/birthday.json'

# full path to file
pathToFile = 'C:/Users/jerom/Documents/GitHub/class-python/birthday/birthday.json'


# try to open a file and throw a error if it is not found
try:
    json_file = open(pathToFile, 'r')
except OSError:
    print('ERROR: Unable to open the file %s' % pathToFile)
    exit(-1)


# read the whole json file into a variable
birthday_list = json.load(json_file)

# create an empty dictionary
birthday_dictionary = {}

# loop json list of data and put each name and birthday into a dictionary
for elem in birthday_list:

    # fetch name and birthday
    name = elem['name']
    birthday = elem['birthday']

    print('name = ' + name)
    print('birthday = ' + birthday)

    birthday_dictionary[name] = birthday


# to print a value in the dictionary by giving it a string with the name as the key
print(f'Jocelyn Jones birthday is {birthday_dictionary['Jocelyn Jones']}')

# to get user input
name = input('Enter a name:')
print('name = ' + name)
