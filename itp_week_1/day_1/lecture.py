# ITP Week 1 Day 1 Lecture

# COMMENTS

# This is a comment line in python.
# Comments start with a '#' sign and Python will ignore them.
# It can be placed on at the beginning of it's own line or at the end of line as well.
# Comments are used to explain code or (ignored) prevent execution while running/testing code.

# Below is an example of code that is ignored/commented out.
# take_candy_from_baby()

# There is a keyboard shortcut to comment/uncomment code.
# Windows: Ctrl + /
# Mac: Cmd + /
# Now let's prevent the code below from running by commenting it out!
# eat_bad_pizza()

##################################
# dont worry about the error     #
# it's because it doesnt exist!  #
##################################

# PRINT

# print is a function provided by python.
# It is an output command, which helps verify any content/code
# by displaying it on the terminal.

# We'll go more into functions later but for now,
# there is the function name followed by parentheses ().
# What goes inside of the parentheses are called arguments.

# This particular function takes the argument and "prints" it to the terminal.

# Replace CHANGE_ME to your favorite color and run the code in your terminal.

# print("BABY BLUE")

# Currently what we're printing is just a string.

# STRINGS

# Strings can be written in single or double quotes.
# There is no difference unless you need to nest one in another.

# Example
'He said "What is your name?"'

'hi this line 1'
'this is line 2'
'this is not efficient'

# Instead of creating multiple different string literals for each line,
# there are two ways to create multiple line strings.
# new-line and multi-line

print("this is an example of using \nnewline, which uses backspace")

"""A multi-line uses tripe quotation marks,
which both single or double doesn't matter
as long as they are the same, at the beginning
and end of the string"""

'''
difvdgbdfjn
dfhb
ftggf
hjg
actual_code()
'''

# practice.py

# VARIABLES

# Variables are containers for storing data values.
# Variables are created when you ASSIGN a value to them.
# Assignment is done with a SINGLE equal sign (=)

# Unlike other programming languages, it doesnt not require a command for declaring a variable.

# my_variable = "a string"

# Rules for variable names
# must start with a letter or the underscore character
# cannot start with a number
# can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# MultiWord Variable Names
# ie. my favorite band
    # 1. MyFavoriteBand - Pascal Case
    # 2. myFavoriteBand - Camel Case
    # 3. my_favorite_band - Snake Case (most used in Python)

# Now, instead of printing string literals, we can print variables which store the string!

name = "Dustin"

# Change the name above to your name and uncomment the line below!

print(name)

# We can combine like-elements, even as variables. (STRING CONCATENATION)

print("Hello my name is " + name)

# INPUT

# A native python function like print which takes in an argument. Native are functions provided by the python language.
# The argument is a string that acts as a prompt which is printed.
# the function waits for the user input.

# We can take the user input and assign it to a variable.

# Review the hello.py to see an example.

user_age = input("What is your age?")

print("Wow, you look good for " + user_age)