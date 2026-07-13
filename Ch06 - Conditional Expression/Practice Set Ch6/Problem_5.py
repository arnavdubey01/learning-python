# Write a program which finds out whether a given name is present in a list or not.

list = ["Harry", "Ravi", "Rohan", "Ogluboglu"]


a = input("Enter your name: ")

print("Enter first letter in capital, as it is case sensitive")

if (a in list):
    print("Your name is in the list")
else: 
    print("Your name is not in the list")