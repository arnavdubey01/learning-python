# A spam comment is defined as a text containing following keywords: “Make a lot of money”,
# “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

#Basically, make a spam filter.


#Note: See how 'in' command works!

comment=input(("Enter the comment: "))

if (("Make a lot of money" in comment) or ("buy now" in comment) or ("subscribe this" in comment) or ("click this" in comment)):
   print("It's a spam.")

else:
   print("It's not a spam.")


#Or I can simply assign variable to each key phrases like p1, p2 ..., 
#then type: if ((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)): ....



#Mistake:  This is not how it works...

# comment=input(("Enter the comment: "))

# if (("Make a lot of money") or ("buy now") or ("subscribe this") or ("click this")) in comment:
#    print("It's a spam.")

# else:
#    print("It's not a spam.")



#Reminder: Python is case sensitive!!