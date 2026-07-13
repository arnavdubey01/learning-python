try:
    a = int(input("Hello! Enter a number: "))
    print(a)


except Exception as e:
    print(e)

finally:
    print("This text is printed under 'finally'")

print("Thank You")

# 'finally' block always runs. If code runs successfully, or throws an exception, it still runs.

# So why not just do print("Text")?
# Well, print text will work similarly, but when defining function, this becomes useful.

def try_finally():
    try:
        a = int(input("Hello! Enter a number: "))
        print(a)


    except Exception as e:
        print(e)

    finally:    
        print("This text is printed under 'finally'")
    
#  Without 'finally:', the "This text..." would not be printed.

    print("Thank You")


try_finally()

# So 'finally' block always runs. Literally. 