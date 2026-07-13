# 8. If languages of two friends are same;
# what will happen to the program in problem 6?
#Let's see:

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

#If value for two keys is same, nothing different happens. value is tied to the key (opposite not true)
#So, two different keys can be assigned same values, with no error or anything.

#Therefore, values can be same.

#Note that when key was same, it's value got updated.

#Conclusion:
# So, the identifier in dictionary is key, not value.