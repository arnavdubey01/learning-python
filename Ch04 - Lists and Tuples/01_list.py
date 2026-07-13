#We can not make changes to existing string. 
#We have to make a new string with the desired changed instead.
#BUT, we can do make changes to list!

friends = ["Apple", "Orange", 5, 345.06, False, "Askash", "Rohan"]
print(friends[0]) #Till here, the output should be 'Apple'

#Let's make changes to this existing list:
friends[0] = "Grapes"
print(friends[0]) #Now, for same command, output will be "Grapes"!

#Therefore, Lists are mutable (Unlike strings)

#Lists can also be indexed, like string:
print(friends[1:4]) #See Output


#List in List is allowed in python.
#Example, a = [["Apple", "Ball"], "Cat", "Dog"]   -   This is valid list.