# ITP Week 2 Day 2 Lecture


#######################
#USER DEFINED FUNCTIONS
#######################
# https://www.w3schools.com/python/python_functions.asp

# "Computer functions are similar to math functions in that they may reference parameters, which are passed, or input into the function."

# USING THE 'DEF' KEYWORD
# https://www.w3schools.com/python/ref_keyword_def.asp

#Use the "def" keyword to define (create) a new function.  Give the function a name, followed by single braces, and a colon.  Indent the following line to run the code in the function body.  The following code will create a function named myNewFunction, and it will print the words "Hello World"

def my_old_function():
    print("Hello")

# "Call" the function to run the code by adding single braces after the name of the function.

my_old_function()

#Functions can accept values and process them in different ways.

#A parameter represents a value that the procedure expects you to pass when you call it. The procedure's declaration defines its parameters.

#An argument represents the value that you pass to a procedure parameter when you call the procedure. The calling code supplies the arguments when it calls the procedure.

def my_new_function(parameter):
    print(parameter)

my_new_function("This is my Argument")

#Functions can have multiple parameters.

def multi_parameter(param1, param2, param3):
    print("My name is " + param1 + " " + param2 + ", and I live in " + param3 + ".")

multi_parameter("Tyler", "Pritchard", "Oakland")

#Function parameters can be any data type, including numbers, booleans, dictionaries, and even other functions!  You can assign your data & functions to different variables, and then tie the varables together in different ways for endless computing possibilities.  Large applications are just many functions contained within different files, all connected in some way and all communicating with each other.  

#The concept of scope rules how variables and names are looked up in your code. It determines the visibility of a variable within the code. The scope of a name or variable depends on the place in your code where you create that variable.

#Global Scope: A variable in the global scope exists outside of functions, and is therefore available to all functions.

my_global_variable = "Joy to the world"

def joy(some_variable):
    print(some_variable)

joy(my_global_variable)

#Local Scope: A variable exists inside of a function, and is therefore NOT accessible to other functions outside of the function where that variable was declared.

def sadness():
    my_local_variable = "John Wick's dog"

#If you uncomment the following function call you will receive the error message 'File "lecture.py", line 54, in <module>
#     joy(my_local_variable)
# NameError: name 'my_local_variable' is not defined"'

#joy(my_local_variable)

#This is because my_local_variable is contained INSIDE the function sadness(), and is therefore not available to any functions outside of that SCOPE.

##############################
# THE PYTHON 'GLOBAL' KEYWORD
#############################
# https://docs.python.org/3/reference/simple_stmts.html#the-global-statement
# https://www.w3schools.com/python/ref_keyword_global.asp

# The 'global' keyword is a keyword that allows a user to modify a variable outside of the current scope. It is used to create global variables from a non-global scope i.e inside a function. Global keyword is used inside a function only when we want to do assignments or when we want to change a variable. Global is not needed for printing and accessing.

# Rules of global keyword:

# If a variable is assigned a value anywhere within the function’s body, it’s assumed to be a local unless explicitly declared as global.
# Variables that are only referenced inside a function are implicitly global.
# We Use global keyword to use a global variable inside a function.
# There is no need to use global keyword outside a function.

x = 4

def global_key():
    global x
    x = 444

global_key()
print(x)


# WHAT IS GLOBAL KEYWORD IN PYTHON?
# "Global keyword is a keyword that allows a user to modify a variable outside of the current scope. It is used to create global variables from a non-global scope i.e inside a function. Global keyword is used inside a function only when we want to do assignments or when we want to change a variable. May 31, 2020" -geeksforgeeks.org

# SHOULD YOU USE GLOBAL IN PYTHON?
# "The way Python uses global and local variables is maverick. ... In most cases where you are tempted to use a global variable, it is better to utilize a parameter for getting a value into a function or return a value to get it out. Like in many other program structures, Python also imposes good programming habit by design.Aug 16, 2021"  -python-course.eu