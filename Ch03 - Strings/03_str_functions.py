name = "arnav"

print(len(name)) # Prints the length of string, here, 5.

print(name.endswith("nav")) #Output comes as "True" because string really ends with "nav"(Arnav).

print(name.startswith("ar")) #Output will be "True", because why not.

#Note that these are case sensitive. name.startswith("Ar") will return "False".


print(name.capitalize()) #This capitalizes the first letter of the first word of string.


# .replace function, used to replace words in string.
b = 'That is a nice car'
print(b.replace("nice", "decent"))  #This replaces "nice" to "decent".

# .count function to count the occurence of any character.
print(b.count("a"))

# .find  - used to return the first index of the word from string:
print(b.find("car"))

#There are MANY MORE functions for string.
#Find more functions using chatgpt or claude.