# ITP Week 1 Day 3 Lecture

# PYTHON COLLECTIONS (ARRAYS)

# There are four collection data types in the Python programming language:

# - List:       ordered and changeable.     Allows duplicate members.
# - Tuple:      ordered and unchangeable.   Allows duplicate members.
# - Set:        unordered and unindexed.    No duplicate members.
# - Dictionary: ordered* and changeable.    No duplicate members.

# *As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning,
# and, it could mean an increase in efficiency or security.

# LIST

# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets:

my_list = ["apple", "banana", "cherry"]

# The example above is stored in a variable called `my_list`.

# List items are ordered, changeable, and allow duplicate values.


# Ordered
    # List items are indexed, the first item has index [0], the second item has index [1] etc.
    # When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
    # If you add new items to a list, the new items will be placed at the end of the list.
    # Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable
    # The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
    # Since lists are indexed, lists can have items with the same value

second_list = ["apple", "apple", "banana", "orange", "banana"]

# List Items - Data Types
    # List items can be of any data type:
        # String, int and boolean data types:

list_1 = ["apple", "banana", "cherry"]
list_2 = [1, 5, 7, 9, 3]
list_3 = [True, False, False]

    # A list can contain different data types:

list_4 = ["abc", 34, True, 40, "male"]
list_5 = [["John", "Smith", 1,2,5,345,34,True,"asdoij"], ["Jane", "Doe"], 123, False]
print(list_5[0][1]) # should return Smith

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':

print(type(list_5)) # <class 'list'>

# len()
# You can retrieve the length of the list by wrapping the data collection with len().

# EX: len(list_5)
print(len(list_5))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

list_6 = list(("apple", "banana", "cherry")) # note the double round-brackets

# ACCESS LIST ITEMS

#            0         1         2         3        4       5         6
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# List items are indexed and you can access them by referring to the index number:

print(fruits[0]) # "apple"

# if i want mangos
mango = fruits[6]

# kiwi
kiwi = fruits[4]

# Negative Indexing
# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

print(fruits[-1]) # "mango"
print(fruits[-7]) # "apple"

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

print(fruits[2:5]) # what does this return?

# NOTE: beginning is included, end is not included.


short_fruits_list = fruits[2:5]

print(type(short_fruits_list)) # list



# By leaving out the start value, the range will start at the first item:

print(fruits[:4]) # "apple", "banana", "cherry", "orange" # NOT INCLUDE KIWI

# By leaving out the end value, the range will go on to the end of the list:

print(fruits[2:]) # "cherry", "orange", "kiwi", "melon", "mango"

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:

print(fruits[-4:-1]) # "orange" (-4) to, but NOT including "mango" (-1)




# To determine if a specified item is present in a list use the `in` keyword:

if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")








# CHANGE LIST ITEMS

# fruits = ["strawberry", "blackcurrant", "watermelon", "orange", "kiwi", "melon", "mango"]
# for reference, without scrolling up..

# To change the value of a specific item, refer to the index number:
fruits[0] = "strawberry"

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values:

fruits[1:3] = ["blackcurrant", "watermelon"]












# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# Change the second value by replacing it with two new values:
more_fruits = ["raspberry", "coconut", "pineapple", 2342, 4554, 324, 4567, 23, 345 , 234,  4534 , 2342]

more_fruits[1:8] = ["grape", "durian"]

print(len(more_fruits)) #

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# Change the second and third value by replacing it with one value

# ADD LIST ITEMS

# Append Items
# To add an item to the end of the list, use the append() method:

sports = ["football","soccer","baseball"]

sports.append("lacrosse")

# Insert Items
# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

sports.insert(1, "basketball") # ["football", "basketball", "soccer", "baseball", "lacrosse"]

# Extend List
# To append elements from another list to the current list, use the extend() method.

more_sports = ["hockey", "water polo"]

sports.extend(more_sports)

more_sports.extend(sports) # ['hockey', 'water polo', 'football', 'basketball', soccer', 'baseball', 'lacrosse']

# REMOVE LIST ITEMS

# Remove Specified Item
# The remove() method removes the specified item.

car_make = ["BMW", "Honda", "Mazda", "Ford", "Ronald McDonald Hamburglar Car"]

car_make.remove("Ronald McDonald Hamburglar Car")

# Remove Specified Index
# The pop() method removes the specified index.

car_make.pop(0) # removes "BMW"

# If you do not specify the index, the pop() method removes the last item.

car_make.pop() # removes "Ford" since we already removed the Hamburglar Car

# The del keyword also removes the specified index:

del car_make[0] # removes "Honda" since we already removed "BMW"

# be careful with the del keyword because if you dont specify an index, it will delete the whole list

del car_make # poof, the list is gone

# print(car_make) # this will cause an error

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

long_important_list = ['imagine', 'this', 'list', 'is', 'filled', 'with', 'important', 'stuff']

long_important_list.clear()

print(long_important_list) # []

# the variable and the list still exists but it will be empty.

# Strings are handled similiarly to list.
    # len()
# String also has native methods(functions)!

string = "daniel"
string.capitalize()
string.upper()
print(string)

# PRACTICE_1

# PYTHON LOOPS

# Python has two primitive loop commands:
    # while loops
    # for loops

# WHILE LOOP

# With the while loop we can execute a set(block) of statements as long as a CONDITION is true.

i = 1
while i < 6:
  print(i)
  i += 1

# NOTE: remember to increment i, or else the loop will continue forever.

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i,
# which we set to 1.

# With the break statement we can stop the loop even if the while condition is true:

j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1

# With the continue statement we can stop the current iteration, and continue with the next:

k = 0
while k < 6:
  k += 1
  if k == 3:
    continue
  print(k)

# With the else statement we can run a block of code once when the condition no longer is true:

l = 100
while l < 100:
  print(l)
  l += 1
else:
  print("l is no longer less than 100")

# (OLD SCHOOL) FOR LOOP

# Java

# for (int i = 0; i < 6; i++) {
#   System.out.println(i);
# }

# JavaScript

# for (let i = 0; i < 6; i++) {
#   console.log(i)
# }

# but this is just counting from 1 to 6 and this doesn't make sense.. (in Python)
# so what do we use for loops? Enter list...

# Java

# String[] stringArray = ["Hello", "World"];

# for (int i = 0; i < stringArray.length; i++) {
#   System.out.println(stringArray[i]);
# }

# JavaScript

# const stringArr = ["Hello", "World"]

# for (let i = 0; i < stringArr.length; i++) {
#   console.log(stringArr[i])
# }

# LOOP (ITERATE) LIST

string_array = ["Hello", "World"]

# PYTHON FOR LOOP

for x in string_array:
    print(x)

names = ["Dan", "John", "Chuck", "Bob"]

for name in names:
  print("Hello " + name)

# NOTE: the x variable can be set to whatever you want
# If we had an array of numbers, I would call a single variable number (singular)
# x is represent the element itself, unlike the index like java or JS

# Well, what if we do need to just count from 1 to 6?

# PYTHON RANGE

# To loop through a set of code a specified number of times,
# we can use the range() function,

# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.

for x in range(6):
  print(x)

# NOTE: range(6) is not the values of 0 to 6, but the values 0 to 5.

# The range() function defaults to 0 as a starting value,
# however it is possible to specify the starting value by adding a parameter:
# range(2, 6), which means values from 2 to 6 (but not including 6):

for x in range(2, 6):
  print(x)

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter:
# range(2, 30, 3):

for x in range(2, 30, 3):
  print(x)

# NOTE: else and break also works here to do a final statement or stop the iteration

# How do we use range with list?
# loop through the index numbers of a list

starter_pokemons = ['charmander', 'squirtle', 'bulbasaur']

for starter_pokemon_index in range(3):
    print(starter_pokemon_index)
    print(starter_pokemons[starter_pokemon_index])

# NOTE: for loops cannot be empty,
# but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass

# BREAKOUT ROOM