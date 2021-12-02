#---------------WORKING WITH OTHER TYPES OF DOCUMENT OBJECTS-------------
# There are many types of document objects, more than can we can cover in one course, but that doesn't mean you won't encouter them in the future.  The purpose of this section is for you to figure out how to handle a situation in which you are tasked with using a new file type.  The following are a couple of common file types.

# JSON:  For those of you who took web development, you may be familiar with the JSON object.  It stands for "Javascript Object Notation", but it is widely used in non-JavaScript applications.  It is a simple way of storing dictionaries and lists in one easily imported and accessible object.

#  https://docs.python.org/3/library/json.html

# JSON Object

# JSON objects are very much like javascript objects.
# JSON objects are written in key/value pairs.
# JSON objects are surrounded by curly braces { }.
# Keys must be strings, and values must be a valid JSON data type (string, number, object, array, boolean or null).
# Keys and values are separated by a colon.
# Each key/value pair is separated by a comma.

# JSON Objects wil have a filename of .json
# The syntax of a JSON object looks like the following:

{"name": "Zophie", "isCat": true,
 "miceCaught": 0, "napsTaken": 37.5,
 "felineIQ": null}


# JSON is useful because it can allow programs to interact with a website.  This is called and API, or Application Program Interface.  Accessing an API is the same as accessing any other web page via a URL. The difference is that the data returned by an API is formatted (with JSON, for example) for machines. 

# Many websites make their data available in JSON format.

# You’ll have to find documentation for what URLs your program needs to request in order to get the data you want, as well as the general format of the JSON data structures that are returned. This documentation should be provided by whatever site is offering the API; if they have a “Developers” page, look for the documentation there.

#Using APIs, you could write programs that do the following:

#   Scrape raw data from websites. (Accessing APIs is often more convenient than downloading web pages and parsing HTML with Beautiful Soup.)
#   Automatically download new posts from one of your social network accounts and post them to another account. For example, you could take your Tumblr posts and post them to Facebook.
#   Create a “movie encyclopedia” for your personal movie collection by pulling data from IMDb, Rotten Tomatoes, and Wikipedia and putting it into a single text file on your computer.
#  You can see some examples of JSON APIs in the resources at https://nostarch.com/automatestuff2/

#  The JSON library for Python is "native", or "built-in", meaning "It comes with Python", however you still must import it into your file before you can begin working with JSON:

import json

# Notice the absence of squigly lines below the 'json'.  That's because you do NOT need to install it.

# JSON Commands:
# There aren't that many, because all you're doing is converting data between two programs.
json.dumps()
# This will allow you to "encode" a data structure (ie, lists, dictionaries, etc) into a format readable by other applications which use JSON.  It will not be easily readable to a human unless you "pretty print" it, by which they mean, use a print statement to look at.
print(json.dumps())

json.loads()
#This will allow you to "decode" JSON objects so that you may use the resulting data




#----------------RegEx----------------
#  You can get by in life just fine without RegEx, but it's nice to have it as a tool in your toolbox of engineering skills.
#RegEx is terrifying to look at.  Don't be afraid!  There are cheatsheets and online tools to help you solve your RegEx propblems.
#RegEx is useful because it allows you to use ambiguous strings and numbers in your CRUD operation.  If you encounter a problem that requires regex, consult: 
# 
# http://www.rexegg.com/

#You will likely need a sandbox to test your code.  Go to:
#
# https://www.regexpal.com/

#BETWEEN THESE TWO TOOLS ^^^ YOU SHOULD BE ABLE TO UTILIZE REGEX IN YOUR PROGRAMS

#But....... Here's a bunch of information about it anyways. If you scan over it you can see, much like working with Git, you can dive as deep as you want into RegEx and there are entire courses dedicated to only RegEx(https://www.udemy.com/course/mastering-regular-expressions-in-javascript/).  The main takeaways from this section of the lecture are that everyone should: 
#
#     Understand, 'What is RegEx?'
#     Bookmark the RegEx tools

# NOW, Here's all that stuff!  This information is for you to refer to in the future if you want to work with RegEx

#REGULAR EXPRESSION BASICS
# Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
# Regex strings often use backslashes (like \d), so they are often written using raw strings: r'\d'
# \d is the regex for a numeric digit character.
# Import the re module first.
# Call the re.compile() function to create a regex object.
# Call the regex object's search() method to create a match object.
# Call the match object's group() method to get the matched string.

#GROUPS AND THE PIPE CHARACTER
# Groups are created in regex strings with parentheses.
# The first set of parentheses is group 1, the second is 2, and so on.
# Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
# Use \( and \) to match literal parentheses in the regex string.
# The | pipe can match one of many possible groups.

#REPETITION IN REGEX PATTERNS AND GREEDY/NON-GREEDY MATCHING
# Greedy: As Many As Possible (longest match)
# By default, a quantifier (see: http://www.rexegg.com/regex-quantifiers.html) tells the engine to match as many instances of its quantified token or subpattern as possible. This behavior is called greedy.

# Lazy: As Few As Possible (shortest match)
# In contrast to the standard greedy quantifier, which eats up as many instances of the quantified token as possible, a lazy (sometimes called reluctant) quantifier tells the engine to match as few of the quantified tokens as needed.

# The ? says the group matches zero or one times.
# The * says the group matches zero or more times.
# The + says the group matches one or more times.
# The curly braces can match a specific number of times.
# The curly braces with two numbers matches a minimum and maximum number of times.
# Leaving out the first or second number in the curly braces says there is no minimum or maximum.
# "Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching") matches the shortest string possible.
# Putting a question mark after the curly braces makes it do a nongreedy/lazy match.

# REGEX CHARACTER CLASS AND THE FINDALL() METHOD
# The regex method findall() is passed a string, and returns all matches in it, not just the first match.
# If the regex has 0 or 1 group, findall() returns a list of strings.
# If the regex has 2 or more groups, findall() returns a list of tuples of strings.
# \d is a shorthand character class that matches digits. \w matches "word characters" (letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
# The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace.
# You can make your own character classes with square brackets: [aeiou]
# A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]

#REGEX DOT-STAR AND CARET/DOLLAR CHARACTER
# ^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
# The . dot is a wildcard; it matches any character except newlines.
# Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
# Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

#REGEX SUB() METHOD AND VERBOSE MODE
# The sub() regex method will substitute matches with some other text.
# Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
# Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
# If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.