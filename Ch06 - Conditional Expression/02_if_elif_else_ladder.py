a = int(input("Enter your age: "))

#if, elif, else ladder:

if(a>=18):
    print("You are above the age of consent")
    print("You are above 18")   #This space which comes in the next line after using column ':', is called indentation. It means that now we are working under the 'if():'

elif(a<0):
    print("Invalid age")

elif(a==0):
    print("Can't be 0!")

else:
    print("You are below the age of consent")

print("End of Program")  #This is not under 'if' or 'else', so it prints at the end whatsoever.


#Note that if, elif and else are connected.
#Python first check 'if:', if it is not true, than it checks all the 'elif:'s, and if 'elif:' conditions are not satisfied either, then it prints the code entered under 'else:'
