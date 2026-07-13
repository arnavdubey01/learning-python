# Dictionary = {
#     "Key1" = value1,
#     "Key2" = value2
# }
# --------------------------------------------------
#Dict = {}  Is an empty dictionary
# --------------------------------------------------
#Example given below:
marks = {
    "Harry" : 100,
    "Rohan" : 60,
    "Ravi" : 42,
    "A" : [1,2,7]
}

print(marks, type(marks))  #This prints dictonary of marks, followed by type, which is dict.

print(marks["Harry"]) #This prints marks of harry only
print(marks["A"]) #Prints list


#Dictionaries are:
#unordered
#mutable (like list, unlike string or tuple)
#indexed
#cannot contain duplicate keys
