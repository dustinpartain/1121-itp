# ITP Week 1 Day 2 (In-Class) Practice

# This is a number magic trick
# Pick a number from 1 - 9
# Multiple by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number
# Final number is 5


# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!

original_number = input("Pick a number from 1-9 ")
int_num = int(original_number) # this converts user input number into an int and stores it in a variable called int_number
step_a = int_num * 2
step_b = step_a + 10
step_c = step_b // 2
step_d = step_c - int_num

if step_d == 5:
    print("wow this number works")
else:
    print("this is a fraud!!!")