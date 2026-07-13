# 7. Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n = int(input("Enter value: "))

for i in range(1, n+1):
    print(" "*(n-i),"*"*(2*i-1))

#Alternatively:

n = int(input("Enter value: "))

for i in range(1, n+1):
    print(" "*(n-i), end="")    #[end=""]; by using this, a new line is not added by default in print output.
    print("*"*(2*i-1), end="")
    print()

# print() adds exactly one newline (\n).
#
# If the previous print used the default end="\n", then print()
# moves to the next line again, creating a visible blank line:
#
#     print("Hello")   -> outputs "Hello\n"
#     print()          -> outputs "\n"
#     print("World")
#
# Result:
#     Hello
#
#     World
#
# But when using end="", no newline is added:
#
#     print("*", end="")   -> outputs "*"
#     print()              -> outputs "\n"
#
# Here print() is the only newline, so the next output starts on
# the very next line and no blank line appears.
#
# print("\n") outputs TWO newlines:
#     1. "\n" from the string itself
#     2. "\n" added automatically by print()
#But since I used print(...,end =()) this end=() removed the usual \n by python which is by default.
#
# Therefore print("\n") leaves an empty line, while print()
# only moves to the next line once.