# We can raise errors in our program.. But why?
# Suppose we made a module in python and upload it.
# Some random guy downloads it and use it.
# Suppose he makes a mistake, then I would like to stop the program.
# So raising this error will crash and stop the program.

# But, program crashing is not good, right?

# Sometimes, program ~should crash, because if another developer is doing some mistake, he or she should know that they have done a critical mistake.

# They will fix it only after knowing it clearly.

a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) # Suppose user enters '0'

if (b == 0):
    raise ZeroDivisionError("Our program is not meant to divide numbers by zero.")

else:
    print(f"The division a/b is {a/b}")