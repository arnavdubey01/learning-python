a = int(input("Enter your age: "))
        

#if-statement no. 1

if(a%2 == 0):   #a%2 == 0 means if a divides by 2 gives remainder 0 (if true)
    print("a is even")

#End of if-statement no. 1

######################################

#if-statement no. 2
if(a>=18):
    print("You are above the age of consent")
    print("You are above 18")   #This space which comes in the next line after using column ':', is called indentation. It means that now we are working under the 'if():'

elif(a<0):
    print("Invalid age")

elif(a==0):
    print("Can't be 0!")

else:
    print("You are below the age of consent")

#End of if-statement no. 2

######################################

#Here now, both if statements run independently and execute seperately.

#note: 'if' can work alone, but 'else' or 'elif' can not work alone (invalid syntax)