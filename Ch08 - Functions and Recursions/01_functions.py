# If a certain task with long code is needed to be done multiple times in acode, 
# we assign it as a function

#we use " def 'function name' ", and whenever we type 'Function name', It performs those full set of commands under that function.

    #define function:
def avg():
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    c=int(input("Enter number: "))
    
    average = ((a+b+c)/3)
    print(average)

avg()   #This is function call
avg()
avg()

#avg() is typed three time, so the code under def avg() will run three times. Basically, we didn't had to type the full code three times.
# We just assigned it as a function named avg, so whenever we want to call it, we just type avg().
#The brackets () are for parameter. Here, there is no parameter.

#We can also use 'return' command:


def avg():
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    c=int(input("Enter number: "))
    
    return ((a+b+c)/3)

print(avg())
print(avg())
print(avg())

#This is more cleaner, and preferred way.