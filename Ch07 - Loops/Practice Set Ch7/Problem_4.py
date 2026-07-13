# 4. Write a program to find whether a given number is prime or not.
n = int(input("Enter the numeber: "))

for i in range(2, n):   #We can not do range(1, n) because than n/i i.e. n/1 will always give 0 remainder, so output will always be "Given number is not prime".
    if (n%i) == 0:   #this means: "If n divided by i gives remainder 0"
        print("Given number is not a prime number.")
        break   #break command is used, or else program will print multiple same outputs.

    else:
        print("Given number is a prime number.")
        break


#Program first puts i = 2, then checks if the use input number (n), on division with i = 2, gives 0 remainder or not.
#If it does, then it is not a prime number.

#Prime numbers are only divisible by themselves and one, i.e, prime numbers on division by themselves or one, gives remainder 0.
#Any other "i", which is not the number itself, or not equal to 1, if on division with the given number, gives remainder 0, implies that the given number is divisible by that "i", making it non-prime.
