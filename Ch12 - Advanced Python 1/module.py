def myFunc():
    print("Hello world!")

myFunc()
print(__name__) #prints __main__

if __name__ == "__main__":  #If this code is directly executed by running the file it is present in.
    print("We are directly running this code")
