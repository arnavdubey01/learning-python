# Write a program to find out whether a given post is talking about “Harry” or not.


post = input("Enter the post: ")

if ("harry" in post.lower()):
    print("The given post talks about Harry.")

else:
    print("The given post does not talk about Harry")

#Note that the .lower() command helps to detect harry keyword without being case sensitive.
#i.e. It will detect haRry or hArry or harry or harry or HArrY or HARRY or harrY or any variation.

#Basically, python converts each uppercase letter in whole post to lowercase. 
#So even if post contains 'HaRrY', python sees it as 'harry' anyways. And since 'harry' is in post, it prints "The given post talks about Harry."


#######################

#Mistake:
#Following programs works, but assumes 0 user error in writing "Harry"
#Now, it does cover 'Harry' and 'harry', but what about something like 'haRry' or 'harrY' or 'hArry'?
#It does not detect those...

post = input("Enter the post: ")

if "Harry" in post or "harry" in post:
    print("The given post talks about Harry.")

else:
    print("The given post does not talk about Harry")