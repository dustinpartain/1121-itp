# ITP Week 2 Day 3 Lecture

# Functions can take lists and dictionaries as arguments. 

myToons = {
    "Tauren": "Druid",
    "Elf": "Mage",
    "Undead": "Warrior",
    "Troll": "Hunter"
}

def pickToon(toons):
    select = input("Which character? \n")
    for toon in toons:
        if toons[toon] == select:
            print(select + " FTW! \n")
            break #skips over the else statement
        #   pass #does nothing
        #   continue #skip this loop and move to the next
        else:
            print("Wrong character")

#pickToon(myToons)

#In Python, Pass, Continue and break are used to loops. Though continue and break are similar to that of other traditional programming languages, pass is a unique feature available in python. break - Terminates the loop, after its invocation. continue - Skips the current loop, and continues perform the next consecutive loops. pass - Does nothing

#Remember DRY (Do not repeat yourself!).  If you find yourself repeating code, assign that code to a variable and then simply use the variable where ever you would have written that function.

# Procedure, Routine, Subroutine
# On Day 2 we created a function that would run two other functions in order to catch a pokemon.  Those two functions, when executed within another function, can each be referred to as a "procedure", "routine", or "subroutine".

def intro():
    print("Welcome to the game!")

def startGame():
    intro()
    pickToon(myToons)

startGame()

# The Python return statement is a key component of functions and methods. You can use the return statement to make your functions send Python objects back to the caller code. These objects are known as the function’s return value. You can use them to perform further computation in your programs.  The Python return statement is a special statement that you can use inside a function or method to send the function’s result back to the caller. A return statement consists of the return keyword followed by an optional return value.

# In general, a function takes arguments (if any), performs some operations, and returns a value (or object). The value that a function returns to the caller is generally known as the function’s return value. All Python functions have a return value, either explicit or implicit.

# An explicit return statement immediately terminates a function execution and sends the return value back to the caller code. 

def add(a, b):
    return a + b

myNumber = add(5, 9)
print(myNumber)

# A Python function will always have a return value. There is no notion of procedure or routine in Python. So, if you don’t explicitly use a return value in a return statement, or if you totally omit the return statement, then Python will implicitly return a default value for you. That default return value will always be None.

# You can use a return statement to return multiple values from a function. To do that, you just need to supply several return values separated by commas.

#Return vs Print:
#Print displays the content to the console, return returns the value to a variable so you can use the value it just returned later in the program. Print is what you see on the console, but the return function is what the computer gets.

# Modularity
# Modular programming (also referred to as modular architecture) is a general programming concept. It involves separating a program’s functions into independent pieces or building blocks, each containing all the parts needed to execute a single aspect of the functionality. Together, the modules make up the executable application program.

# The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool.

#You can import modules and get access to new functions.

#Absolute Path: Absolute path specifies the location from the root directory.

#This is the ABSOLUTE path to this file on my computer:
#  /Users/tylerpritchard/Desktop/VIT/day_3/lecture.py

#Relative Path: A relative path is related to the current directory

#This is the RELATIVE path to this file on my computer:
#  day_3/lecture.py

#----------MODULES------------
# The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool.

#You can import modules and get access to new functions.

#---------USING PATHS TO CONNECT THINGS----------
#Absolute Path: Absolute path specifies the location from the root directory.

#This is the ABSOLUTE path to this file on my computer:
#  /Users/tylerpritchard/Desktop/VIT/day_3/lecture.py

#Relative Path: A relative path is related to the current directory

#This is the RELATIVE path to this file on my computer:
#  day_3/lecture.py


#--------------IMPORTING MODULES---------
#Use the "import" keyword to bring outside functions/programs into the file you are currently working on.  For example, to add additional math functionality to your file, import the "math" module.
import math

#Now you can use math functions that were not previously available, like:

num1 = math.sqrt(16)
print("num1 is ", num1)

num2 = math.pi
print("num2 is ", num2)

tip = math.sinh(num2)
print(tip)