# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
#Let's try:

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

#Conclusion:
#The value of the same key is updated. So the value of the same name is considered the one entered latest.