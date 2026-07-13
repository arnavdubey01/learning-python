# 2. Write a python program using function to convert Celsius to Fahrenheit.

#Formula is:  c/5 = (f-32)/9. therefore, f = (9c/5) + 32

def tempConversion():
    c = float(input("Enter temperature in Celsius: "))      #Used 'float' instead of 'int' to accept decimal values in celcius too.
    return (f"{c}°C = {((9*c)/5) + 32}°F")    

print(tempConversion())



#Alternatively,



def tempConversion(c):
    return (9*c)/5 + 32    

c = float(input("Enter temperature in Celsius: "))      #again, #Used 'float' instead of 'int' to accept decimal values in celcius too.
f = tempConversion(c)

print(f"{c}°C = {round(f, 2)}°F")  #'round' fucntion is used to round off the result. the ', 2' in {round((9*c)/5) + 32, 2} represents: round upto 2 decimal places.