try:
    a = int(input("Hello! Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("This text is printed under 'else'")


print("Thank You")

# 'else' runs only when 'try' is successful. 