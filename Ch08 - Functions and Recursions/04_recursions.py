# Recusrsion is a function which calls itself.

#Factorial:
# n! = n * (n-1)!

#Following is a recursion.
def factorial(n):
    if n==1 or n==0:            #This is called base condition, this is important as without this, recursion will show error due to calling itself infintely.
        return 1                #It basically gives a base for the program to end upon.
    
    a = n * factorial(n-1)      #See how the function that was being defined itself is used in the function 'n * factorial(n-1)'. (This makes this function a recusrsion)
    return a



print(factorial(5))
#or,
print(factorial(n = int(input("Enter number: "))))

#This basically works as:

# 5! = 5*4! = 5*4*3! = 5*4*3*2! = 5*4*3*2*1! = 5*4*3*2*1

#So recursion makes things easy, but a small mistake can cause recursion to call itself infinitely.
#For example, if we don't do 'if n==1 or n==0: return 1, the recursion will give RecursionError: maximum recursion depth exceeded.