# 3. How do you prevent a python print() function to print a new line at the end?

#Take a look at Problem 7 and Problem 9 of Practice Set of Chapter 7 - Loops.

print("a")            #new line added by default
print("b")            #new line added by default
print("c", end="")    #no new line is added because of end="", so it directly prints next command in same line
print("d")

#end="" is used to prevent addition of the default new line added by 'print' function.