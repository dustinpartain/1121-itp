# ITP Week 2 Day 2 (In-Class) Practice

# Functions I

#Write a function called use_poke_ball to print the text "You threw a poke ball!" and then call that function.

#input
# none

# Define function
def use_poke_ball():
    #print text
    print("You threw a pokeball!")

#output
# string

#call function
use_poke_ball()

#Write a function called catch_pokemon that takes a single parameter named favorite, and then prints the words "You caught a " + the name of your favorite pokemon.  Remember to write the function with a single parameter, and then call the function using a string as the arguement.

#input
# string

#Define single parameter function, called favorite
def catch_pokemon(favorite):
    #print text
    print(f"You caught a {favorite}!")

#call function
catch_pokemon("Ryachu")

#output
# string



#Write a SINGLE function defined as catchem_all that runs the TWO function calls you already wrote.  When you run the catchem_all function it should run the TWO functions and print:
#"You threw a poke ball!"
#"You caught a <Ryachu>"

#input
# string

#Define function - cathem_all
def catchem_all(pokemon):

#call function 1 - use pokeball
    use_poke_ball()
#function 2 - catch pokemon
    catch_pokemon(pokemon)

catchem_all("Pikachu")
#call function

#output
# string


#Let's re-write the catch pokemon function so it's more fun.  Delete the contents of the catch_pokemon function and the function's parameter.  Outside of the catch_pokemon FUNCTION, create a string input and assign it to a variable called pokemon.  For the input question, use the prompt "What did you catch?"  Now let's re-write the print statement, but this time have it print out the pokemon input by the user.