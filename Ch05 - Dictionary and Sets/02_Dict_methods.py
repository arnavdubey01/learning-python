marks = {
    "Harry" : 100,
    "Rohan" : 60,
    "Ravi" : 42,
    "A" : [1,2,7],
    0 : "Aman"         # - This can also be done  
}

print(marks.items())

print(marks.keys())

print(marks.values())

#To update the dictionary:
marks.update({"Harry": 99})   #Since dictionary is mutable, it updates.
print(marks)   #Harry's marks updates from 100 to 99.

#We can use same command to add keys and corresonding values:
marks.update({"Renuka": 90})
print(marks)

#Now:
print(marks.get("Harry"))
print(marks["Harry"])
#Clearly, these two commands return exactly same output. So what is the difference??
#See:

print(marks.get("Harry2"))    #Prints None
#print(marks["Harry2"])        #Prints Keyerror

#Since "Harry2" does not exist in the list, marks.get command will return "None".
#While the marks["Harry2"] command will return error.
#That is the difference!

print(marks.clear())  #Empties the dictionary.

print(len(marks)) #This prints Length of dictionary. Since we used .clear just above, output comes to be 0 this time.

# More commands like- .copy, .keys, .pop, .popitem and many more. Use ChatGPT