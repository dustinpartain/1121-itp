
# def my_old_function():
#     print("Hello")

# def my_new_function(parameter):
#     print(parameter)

# my_new_function("This is my Argument")

# def multi_parameter(param1, param2, param3):
#     print("My name is " + param1 + " " + param2 + ", and I live in " + param3 + ".")

# multi_parameter("Tyler", "Pritchard", "Oakland")

# def multi_parameter(param1, param2, param3):
#     #print("My name is " + param1 + " " + param2 + ", and I live in " + param3 + ".")
#     print(f"My name is {param1} {param2} and I live in {param3}.")
# multi_parameter("Tyler", "Pritchard", "Oakland")

# def use_poke_ball():
#     #print text
#     print("You threw a pokeball!")

# #output
# # string

# #call function
# use_poke_ball()

# #Write a function called catch_pokemon that takes a single parameter named favorite, and then prints the words "You caught a " + the name of your favorite pokemon.  Remember to write the function with a single parameter, and then call the function using a string as the arguement.

# #input
# # string

# #Define single parameter function, called favorite
# def catch_pokemon(favorite):
#     #print text
#     print(f"You caught a {favorite}!")

# #call function
# catch_pokemon("Ryachu")

def use_poke_ball():
    #print text
    print("You threw a pokeball!")

def catch_pokemon(favorite):
    #print text
    print(f"You caught a {favorite}!")

#Define function - cathem_all
def catchem_all(pokemon):

#call function 1 - use pokeball
    use_poke_ball()
#function 2 - catch pokemon
    catch_pokemon(pokemon)

catchem_all("Pikachu")