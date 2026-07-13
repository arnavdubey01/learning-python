# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

d = {}

name = input("Enter Friend's name: ")
lang = input("Enter Favourite language: ")
d.update({name : lang})

name = input("Enter Friend's name: ")
lang = input("Enter Favourite language: ")
d.update({name : lang})

name = input("Enter Friend's name: ")
lang = input("Enter Favourite language: ")
d.update({name : lang})

name = input("Enter Friend's name: ")
lang = input("Enter Favourite language: ")
d.update({name : lang})


print(d)

#------------------------------------------------------------

#I had a doubt: How are we using same variables 'name' and 'lang' multiple times for different entries, and not getting any error
#Well, this is because Because:
# variables in Python can be reassigned.
# Each time you do:

# name = input("Enter Friend's name: ")

# the variable name simply gets a new value, replacing the old one.

# Same for lang.

# The important part is this line:

# d.update({name: lang})

# At that moment, the current values of name and lang are added to the dictionary d.
# Once added, the dictionary keeps them safely stored, even if the variables later change.

# Variables are reusable
# Reassigning a variable is normal in Python
# The dictionary stores copies/references of the values independently



# ------------------------------------------------------------

#Mistake

#I did this while assuming that program already knew friend's name. But the actual solution also asked to enter friend's name.
# name = {}

# a = input("Harry's favourite language: ")
# name.update({"Harry" : a})

# b = input("Aman's favourite language: ")
# name.update({"Aman" : b})

# c = input("Arnav's favourite language: ")
# name.update({"Arnav" : c})

# d = input("Rohan's favourite language: ")
# name.update({"Rohan" : d})

# print(name)




