import json

# full path to file
pathToFile = r'C:\NGOCS\NGOC\CIS-024C Python\Lupes-Lookup-App\birthday.json'

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
