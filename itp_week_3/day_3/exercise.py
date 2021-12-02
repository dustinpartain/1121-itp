# create a list of dictionaries with peoples basic information

{
    "first_name": "Bob",
    "last_name": "Dylan",
    "age": 23
}

# save to an excel spreadsheet


# Project 1: Reading Data from a Spreadsheet
# Say you have a spreadsheet of data from the 2010 US Census and you have the boring task of going through its thousands of rows to count both the total population and the number of census tracts for each county. (A census tract is simply a geographic area defined for the purposes of the census.) Each row represents a single census tract. We’ll name the spreadsheet file censuspopdata.xlsx, and you can download it from https://nostarch.com/automatestuff2/. Its contents look like Figure 13-2.

# image
# Figure 13-2: The censuspopdata.xlsx spreadsheet

# Even though Excel can calculate the sum of multiple selected cells, you’d still have to select the cells for each of the 3,000-plus counties. Even if it takes just a few seconds to calculate a county’s population by hand, this would take hours to do for the whole spreadsheet.

# In this project, you’ll write a script that can read from the census spreadsheet file and calculate statistics for each county in a matter of seconds.

# This is what your program does:

# Reads the data from the Excel spreadsheet
# Counts the number of census tracts in each county
# Counts the total population of each county
# Prints the results
# This means your code will need to do the following:

# Open and read the cells of an Excel document with the openpyxl module.
# Calculate all the tract and population data and store it in a data structure.
# Write the data structure to a text file with the .py extension using the pprint module.