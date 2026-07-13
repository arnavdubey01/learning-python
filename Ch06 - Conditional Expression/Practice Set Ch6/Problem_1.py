 #Write a program to find the greatest of four numbers entered by the user.

a=int(input("Enter number: "))
b=int(input("Enter number: "))
c=int(input("Enter number: "))
d=int(input("Enter number: "))

if(a>b and a>c and a>d):
    print(a, "is largest")

elif(b>a and b>c and b>d):
    print(b, "is largest")
    
elif(c>a and c>b and c>d):
    print(c, "is largest")

elif(d>a and d>c and d>b):
    print(d, "is largest")

#'and' is used here