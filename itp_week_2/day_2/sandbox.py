
# # def my_old_function():
# #     print("Hello")


# # my_old_function()

# # def my_new_function(parameter):
# #     print(parameter)

# # my_new_function()


# #manaually coded arguments
# person = {
#     "first": "Tyler",
#     "last": "Pritchard",
#     "location": "oakland"  
# }


# def multi_parameter(first_name, last_name, city):
#     # print("My na+ first_name + me is "  " " + last_name + ", and I live in " + city + ".")
#     print(f"My name is {first_name} {last_name} and I live in {city}.")
#     print(first_name)

# def fail(first_name):
#     print(first_name)

# fail(person["first"])


# # print(person)
# multi_parameter(person["first"], person["last"], person["location"])

# # num1 = 9
# # num2 = 5

# # def runFunction(param1, param2):
# #     print(param1 + param2)
    
# # runFunction(num1, num2)




my_global_variable = "Joy to the world"

def joy(some_variable):
    print(some_variable)

# joy(my_global_variable)

#Local Scope: A variable exists inside of a function, and is therefore NOT accessible to other functions outside of the function where that variable was declared.

def sadness():
    my_local_variable = "John Wick's dog"
    joy(my_local_variable)

sadness()


















