# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.

print("Enter marks out of 100")
a = int(input("Enter the marks in Physics: "))
b = int(input("Enter the marks in Chemistry: "))
c = int(input("Enter the marks in Maths: "))

if a>100 or b>100 or c>100:
    print("Please enter valid marks")

else:
    total = ((a+b+c)/3)

    if (total>=40 and a>=33 and b>=33 and c>=33):
        print("congratulations! you passed.")
        print("Percentage: ",total)
    else:
        print("You failed.")
        print("Percentage: ",total)



#Always keep name of variables descriptive. Like: 'Total'; not 't', even if it is long.


#Mistake: Didn't use 'or' and 'and', made the program lengthy for no reason.
# print("Enter marks out of 100")
# a = int(input("Enter the marks in Physics: "))
# b = int(input("Enter the marks in Chemistry: "))
# c = int(input("Enter the marks in Maths: "))


# if(a>100):
#     print("Invalid")
# elif(a>=33):
#     print("You passed in Physics")
# else:
#     print("You failed in Physics")

# if(b>100):
#     print("Invalid")
# elif(b>=33):
#     print("You passed in Chemistry")
# else:
#     print("You failed in Chemistry")

# if(c>100):
#     print("Invalid")
# elif(c>=33):
#     print("You passed in Maths")
# else:
#     print("You failed in Maths")

# total = ((a+b+c)/3)
# if(total>100):
#     print("Please enter marks correctly")
# elif(total >= 40):
#     print("You are passed with ",total,"%")
# else:
#     print("Result: Fail")
#