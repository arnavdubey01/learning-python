# 1. Write a program to open three files 1.txt, 2.txt and 3.txt. 
# If any of these files are not present, 
# a message without exiting the program must be printed prompting the same.


# Suppose files 2.txt and 3.txt do not exist.

try:
    with open("1.txt", "r") as f:  
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thank You!")


# To run correctly (Existing file '1.txt' gets read):

# Explorer -> practice set Ch12 -> open with VSCode

# or

# line 6:
# with open(r"C:\Users\arnav\OneDrive\Documents\GitHub\learning-python\Ch12 - Advanced Python 1\practice set Ch12\1.txt", "r") as f: