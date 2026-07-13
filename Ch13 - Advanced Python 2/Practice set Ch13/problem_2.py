# 2. Write a program to input name, marks and phone number of a student 
# and format it using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input("Enter name: ")
marks = int(input("Enter marks: "))
number = int(input("Enter numeber: "))

a = ("The name of the student is {0}, his marks are {1} and phone number is {2}".format(name, marks, number))

print(a)