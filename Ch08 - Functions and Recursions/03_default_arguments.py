def greet(name, ending="Thank you"):
    print(f"Good Day, {name}")  #Same as: print("Good Day, + "name)
    print(ending)

greet("Arnav")

#Here, we did: def greet(name, ending="Thank you"),
## This ending="Thank you" is interpreted as default value of 'ending' parameter.
#If it was greet(name, ending) only, and then 'greet("Arnav")', it would have returned TypeError saying "greet() missing 1 required positional argument: 'ending'"

#Basically, even if there is no value assigned to parameter 'ending', it by default takes ending="Thank you"
#But if value is provided, like: 'greet("Arnav, "Thanks!!"), it prints the provided value "Thanks!!" instead for 'ending'.
