# 5. Write a python function to print first n lines of the following pattern.
# ***
# **
# *
# - for n = 3

def pattern(n):
    if n==0:
        return      #just type 'return' with nothing else to end program, so, when n==0, end program 
    print(n*("*"))
    pattern(n-1)

n = int(input("Enter number: "))
(pattern(n))





#Mistake: Used "return" instead of print
def pattern(n):
    if n==0:
        return          #just type 'return' with nothing else to end program, so, when n==0, end program 
    return (n * "*")
    pattern(n-1)

n = int(input("Enter number: "))
pattern(n)

# GPT Explains:

# The key idea is that print() and return are different things.

# print(...) displays something on the screen.
# return ... sends a value back to whoever called the function.

# Let's use a very simple example.

# def hello():
#     print("Hi")

# Now call it:

# hello()

# Output:

# Hi

# Why? Because the function itself contains a print("Hi").

# But what does hello() return?

# result = hello()
# print(result)

# Output:

# Hi
# None

# Here's what happened:

# hello() runs.
# It prints "Hi".
# It reaches the end of the function without a return.
# Python automatically returns None.
# result becomes None.
# print(result) prints None.
# Your pattern() function
# def pattern(n):
#     if n == 0:
#         return
#     print(n * "*")
#     pattern(n - 1)

# When you do:

# pattern(3)

# Python executes:

# ***
# **
# *

# and then returns None.

# So:

# print(pattern(3))

# is really like:

# temp = pattern(3)   # prints the stars
# print(temp)         # temp is None

# Output:

# ***
# **
# *
# None
# Compare with a function that returns a value
# def square(x):
#     return x * x

# Now:

# square(5)

# returns 25, but doesn't print anything.

# You won't see any output in a script unless you do:

# print(square(5))

# Output:

# 25
# Visual comparison
# Function that prints
# def f():
#     print("Hello")
# Code	Output
# f()	Hello
# print(f())	Hello then None

# because f() returns None.

# Function that returns
# def g():
#     return "Hello"
# Code	Output
# g()	nothing shown
# print(g())	Hello

# because g() returns "Hello" and print() displays it.

# Think of it this way:

# print() = show a value
# return = give a value back

# Your pattern() function shows stars but gives back nothing (None), so print(pattern(n)) prints the stars and then prints the returned value None.