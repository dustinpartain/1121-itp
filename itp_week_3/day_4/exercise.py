# Project2: Updating a Spreadsheet

# In this project, you’ll write a program to update cells in a spreadsheet of produce sales. Your program will look through the spreadsheet, find specific kinds of produce, and update their prices. Download this spreadsheet from https://nostarch.com/automatestuff2/. Figure 13-3 shows what the spreadsheet looks like.

# image
# Figure 13-3: A spreadsheet of produce sales

# Each row represents an individual sale. The columns are the type of produce sold (A), the cost per pound of that produce (B), the number of pounds sold (C), and the total revenue from the sale (D). The TOTAL column is set to the Excel formula =ROUND(B3*C3, 2), which multiplies the cost per pound by the number of pounds sold and rounds the result to the nearest cent. With this formula, the cells in the TOTAL column will automatically update themselves if there is a change in column B or C.

# Now imagine that the prices of garlic, celery, and lemons were entered incorrectly, leaving you with the boring task of going through thousands of rows in this spreadsheet to update the cost per pound for any garlic, celery, and lemon rows. You can’t do a simple find-and-replace for the price, because there might be other items with the same price that you don’t want to mistakenly “correct.” For thousands of rows, this would take hours to do by hand. But you can write a program that can accomplish this in seconds.

# Your program does the following:

# Loops over all the rows
# If the row is for garlic, celery, or lemons, changes the price
# This means your code will need to do the following:

# Open the spreadsheet file.
# For each row, check whether the value in column A is Celery, Garlic, or Lemon.
# If it is, update the price in column B.
# Save the spreadsheet to a new file (so that you don’t lose the old spreadsheet, just in case).