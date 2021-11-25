#An empyt python file for taking notes, running live code, etc


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }



# car["model"] = "Explorer"
# car["year"] = 1985
# car["wheels"] = 4

# # print(car)

# myCars = ["Camry", "Prius", "Hybrdid"]

# myfamily = {
#   "child1" : {
#     "name" : "Jim",
#     "year" : 1997,
#     "sports": {
#       "baseball": True,
#       "basketball": False
#     }
#   },
#   "child2" : {
#     "name" : "Jane",
#     "year" : 2010
#   },
#   "child3" : {
#     "name" : "John",
#     "year" : 2004
#   }
# }
# #  In order to access a value within a dictionary that is within another dictionary, we simply chain them together like so:
# myfamily.update({"child1": None})

# print(myfamily)



inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}


# Input: Dictionary "inventory"

# Loop through dictionary
for item in inventory:
# Access each KEY / Subtract each VALUE by 1 /Update Keypairs
    inventory[item] = inventory[item] - 1

# Output: Same as input

person_1 = {
    "first_name": 2,
    "favorite_snack": 3,
    "wears_glasses": 1
    }

for item in list(person_1):
# Access each KEY / Subtract each VALUE by 1 /Update Keypairs
    print(person_1[item], "Item BEFORE update")
    person_1[item] = person_1[item] - 1 
    print(person_1[item], "AFTER update")
# If dictionary value is zero
    if person_1[item] == 0:
# Delete dictionary value
        person_1.pop(item)
print(person_1)


















