# a = int(input("Hello! Enter a number: "))
# # print(a)    

# Suppose user enters a string instead of integer
# Now, the program will return an error.
# But, we know that error in a program is not good.

# We will replace this error output with something like "Please enter valid number)"....

# We use 'try' acceptor
try:
    a = int(input("Hello! Enter a number: "))
    print(a)

except Exception as e:
    e = ("Please enter valid number")
    print(e)

print("Thank You")

# See how program doesn't break like it does after an error (user typed str intead of int)

# *We can also handle specific individual error:


# try:

# except ZeroDivisionError:

# except TypeError:

# except:
# All other exception

try:
    a = int(input("Hello! Enter a number: "))
    print(a)

except ValueError as v: # A particular exception
    print(v)

except Exception as e:
    print(e)    #or: print("Please enter a valid number")

print("Thank You")