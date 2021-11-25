# ITP Week 2 Day 2 (In-Class) Practice

# Functions I

#Write a function called use_poke_ball to print the text "You threw a poke ball!" and then call that function.

#input
# none



#output
# string

#call function
# use_poke_ball()


#Write a function called catch_pokemon that takes a single parameter named favorite, and then prints the words "You caught a " + the name of your favorite pokemon.  Remember to write the function with a single parameter, and then call the function using a string as the arguement.

#INPUT: string


# Call function
# catch_pokemon("Ryachu")

#OUTPUT: string

#Write a SINGLE function defined as catchem_all that runs the TWO function calls you already wrote.  When you run the catchem_all function it should run the TWO functions and print:
#"You threw a poke ball!"
#"You caught a <Ryachu>"

# INPUT: string
# define function- catchemall
# Define function



def use_poke_ball():
    print("You threw a pokeball!")



#INPUT: String
#User input GLOBAL


def catch_pokemon(favorite):
    print(f"You caught a {favorite}")
    

#OUTPUT: STRING


#Let's re-write the catch pokemon function so it's more fun.  Delete the contents of the catch_pokemon function and the function's parameter.  Outside of the catch_pokemon FUNCTION, create a string input and assign it to a variable called pokemon.  For the input question, use the prompt "What did you catch?"  Now let's re-write the print statement, but this time have it print out the pokemon input by the user.

    
def catchemall():
    pokemon = input("What did you catch?")
    use_poke_ball()
    catch_pokemon()

catchemall()

# call the function
#OUTPUT: string
