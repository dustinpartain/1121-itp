# ITP Week 2 Day 1 Lecture

# Review: Day 4 Exercise

#############################
# PYTHON COLLECTIONS (ARRAYS)
#############################

# There are four collection data types in the Python programming language:

# - List:       ordered and changeable.     Allows duplicate members.
# - Dictionary: ordered* and changeable.    No duplicate members.
# - Tuples: covered later this week
# - Sets: covered later this week

#########
# LIST
#########
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.

#################
# DICTIONARY
#################
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:

my_car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021,
  "interest": 22
}

# Dictionary items are ordered, changeable, and does not allow duplicates.

print(my_car)

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

print(my_car["year"])

# Imagine a bank vault, each "item" (element) is a container with a value
# in it. but that "value" (certificates, money, will) is worthless if you
# you can't access it! So the KEY is a pair to the value.

# Ordered or Unordered?

# As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.

# When we say that dictionaries are ordered, it means that the items have a defined order,
# and that order will not change.
# Unordered means that the items does not have a defined order,
# you cannot refer to an item by using an index.

# Changeable
    # Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
    # Dictionaries cannot have two items with the same key:

# Dictionary Length
# To determine how many items a dictionary has,
# use the len() function.

print(len(my_car))
number_of_my_car_keys = len(my_car)

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

# String, int, boolean, and list data types:

your_car = {
  "brand": "Toyota",
  "model": "Pruis",
  "electric": True,
  "year": 2012,
  "colors": ["red", "white", "blue"]
}

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

your_car['brand']

# and of course, by itself, it does nothing
# so we want to assign it to a variable

your_car_brand = your_car['brand']

# why do we assign a variable from the dictionary
# Instead of just typing out the string again?

# There is also a method called get() that will give you the same result:

your_car_brand = your_car.get('brand')

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

key_list = your_car.keys()
print(key_list) # dict_keys(["brand", "model", "electric", "year", "color"])
print(type(key_list)) # <class 'dict_keys'>*

# Get Values
# The values() method will return a list of all the values in the dictionary.

value_list = your_car.values()
print(value_list) # dict_values(['Toyota', 'Pruis', True, 2012, ['red', 'white', 'blue']])
print(type(value_list)) # <class 'dict_values'>*

# Get Items
# The items() method will return each item in a dictionary,
# as tuples* in a list.

item_list = your_car.items()
print(item_list) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
print(type(item_list)) # <class 'dict_items'>*

# A VIEW/REFERENCE TO THE OBJECT NOT COPY

# The list of the key and values is a view of the dictionary,
# meaning that any changes done to the dictionary will be
# reflected in the values list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.values()
z = car.items()

# before the change
print(x)
print(y)
car["condition"] = "fair" # new key created
car["year"] = 2018

#after the change
print(x)
print(y)
print(z)

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")

# Change Values
# You can change the value of a specific item by referring to its key name:

car['year'] = 2019

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

car.update({"year": 2020})

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

car['color'] = "red"

# Same as changing it, but what's really happening in both
# It looks to see if the key exist, if it does, updates the value
# if not, create a new one key:value pair! NO DUPLICATES.

# Update Dictionary
# The update() method will update the dictionary with the items
# from a given argument. If the item does not exist, the item will be added.

# The argument must be a dictionary, or an iterable object
# with key:value pairs.

person_bob = {
    "first_name": "Robert",
    "last_name": "Smith",
    "Nickname": "Bob",
    "age": 41,
    "DOB": "1/2/80"
}

# New dictionary for lesson

# Removing Items
# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name:

person_bob.pop('DOB')

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

person_bob.popitem()

# The del keyword removes the item with the specified key name:

del person_bob["age"]

# NOTE: The del keyword can also delete the dictionary completely:

# del person_bob

# The clear() method empties the dictionary:

person_bob.clear()

# Practice

# DICTIONARY LOOP
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary,
# the return value are the keys of the dictionary,
# but there are methods to return the values as well.

some_dict = {}

# Print all KEY names in the dictionary, one by one:

for x in some_dict:
  print(x)

# Print all VALUES in the dictionary, one by one:

for x in some_dict:
  print(some_dict[x])

# DICTIONARY SUB-LIST*

# You can also use the values() method to return values of a dictionary:

for x in some_dict.values():
  print(x)

# You can use the keys() method to return the keys of a dictionary:

for x in some_dict.keys():
  print(x)

# Loop through both keys and values, by using the items() method:

for x, y in some_dict.items():
  print(x, y)

# NESTED DICTIONARIES 
# Dictionaries can contain other dictionaries, which can contain other dictionaries, which can contain other dictionaries...
myfamily = {
  "child1" : {
    "name" : "Jim",
    "year" : 1997
  },
  "child2" : {
    "name" : "Jane",
    "year" : 2010
  },
  "child3" : {
    "name" : "John",
    "year" : 2004
  }
}
#  In order to access a value within a dictionary that is within another dictionary, we simply chain them together like so:
print(myfamily["child1"]["name"])

#  Here is one way to access values to create your own data structures 
for i in myfamily:
  print(myfamily[i].values())


######################
# TUPLES AND SETS
######################
# - Tuple: Ordered, unchangeable, and INDEXED Allows duplicate members.
#SYNTAX:
gardenPlants = ("lettuce", "raspberry", "cauliflower")

#Access item:
print(gardenPlants[1])

# - Set: Sets are used to store multiple items in a single variable.  Unordered and unindexed. No duplicate members.  
#SYNTAX:

myImmediateFamily = {"Jane", "John", "Jim", "Jen"}

#You must use a for-in loop to access items.
for member in myImmediateFamily:
    print(member)

#You CAN add values to a set using the add() method
myImmediateFamily.add("Adopted")

print(myImmediateFamily)