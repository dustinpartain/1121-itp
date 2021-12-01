# ITP Week 2 Day 3 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers

def subtraction(first_integer, second_integer):
    x = second_integer - first_integer
    print(x)

subtraction(5, 10)

# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

def addition(first_integer, second_integer, third_integer):
    x = second_integer + first_integer + third_integer
    print(x)

addition(5, 7, 10)

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

print("Bill Splitter")

total_bill = float(input("What is the total bill?: "))

percentage_tip = int(input("What % tip would you like to give?: "))

number_of_people = int(input("How many people are splitting the bill?: "))
print("\n")

payment_per_person = ("%.2f" % round(float(((percentage_tip / 100 +1) * total_bill) / number_of_people), 2))

tip_amount = "%.2f" % float(percentage_tip / 100 * total_bill)
print(f"Tip amount: ${tip_amount}")

total_bill_float = float(total_bill)
tip_amount_float = float(tip_amount)
tip_and_total = (total_bill_float+tip_amount_float)
print(f"Total bill including tip: ${tip_and_total}")

print(f"Each person owes: ${payment_per_person}")
