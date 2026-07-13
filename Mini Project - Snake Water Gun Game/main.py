
# 1 for snake
#-1 for water
# 0 for gun

import random           #To randomize bot's decision

snake = 1
water = -1
gun = 0

print("s = snake\nw = water\ng = gun")

bot = random.choice([1, -1, 0])     #Command from imported 'random'
you_input = input("Enter Choice: ")
you_dict = {"s" : 1, "g" : 0, "w" : -1}
rev_dict = {1 : "snake", -1 : "water", 0 :"gun"}
you = you_dict[you_input]



print(f"You chose: {rev_dict[you]} / bot chose {rev_dict[bot]}")

if you == bot:
    print("Draw")

else:
    if bot == 1 and you == -1:
        print("You lose")
    elif bot == 1 and you == 0:
        print("You win")
    elif bot == -1 and you == 1:
        print("You win")
    elif bot == -1 and you == 0:
        print("You lose")
    elif bot == 0 and you == -1:
        print("You win")
    elif bot == 0 and you == 1:
        print("You lose")
    else:
        print("Error")


#It works!