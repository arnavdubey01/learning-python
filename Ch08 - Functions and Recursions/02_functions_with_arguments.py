def greet(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "End of Program"

greet("Arnav", "Thank you")     #(name, ending) --> ("Arnav", "Thank you")
greet("Rohan", "Thanks")
greet("Harry", "")


a = greet("Ravi", "Thanks!")
print(a)    #This also returns "End of Program".
#Return value assigns to a variable, here, a. So when printing 'a', return value also get printed.

