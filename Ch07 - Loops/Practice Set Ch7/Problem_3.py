# 3. Write a program to print multiplication table of a given number using while loop.

n = int(input("Enter the number: "))

i = 1

while(i < 11):
    print(f"{n} * {i} = {n*i}")     #Same as: print(n,"*",i,"=",(n*i))
    i += 1

#We can make it a bit more advanced...

n = int(input("Enter the number: "))
upto = int(input("Enter highest multiplier: "))

i = 1

while(i <= upto):
    print(f"{n} * {i} = {n*i}")     #Same as: print(n,"*",i,"=",(n*i))
    i += 1