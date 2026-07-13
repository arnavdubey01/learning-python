friends = ["Apple", "Orange", 5, 345.06, False, "Askash", "Rohan"]
print(friends)


friends.append("Arnav")  #Append means to add (jodna), so it just adds the thing to the end of list.
print(friends) 


l1 = [1, 2, 54, 96, 11]
l1.sort()  #This sorts the list in increasing order
print(l1)


l1.reverse() #This simply reverses the list and prints.
print(l1) 
#Notice how it printed in descending order, which is actually the reverse of the increasing order, which we just did by using .sort command.
#If we had not used l1.sort(), the output for l1.reverse() would have been '[11, 96, 54, 2, 1]'


#Since .append only adds to the end, to add in between, we use .insert
l1.insert(3, 214)  #Basically, this is command to insert '214' at third index.
print(l1)
                   #So we inserted 214 in the list such that its index is 3


a = l1.pop(3)  #It basically removes, or "pops out" the element at index 3 - list.pop(<index>)
print(l1)
#Since we had 214 on index 3, which we added in the last command (just above this), it got removed using .pop

#I did 'a = l1.pop', instead of simply 'l1.pop', to show this:
print(a) #This is similar to print(l1.pop(3)), it returns the element, which would be removed, or "popped"



#See how we are just changing the original list we created? We can not do same with string (immutable).


l1.remove(96) #This removes the element '96' from the list.
print(l1)
#This is similar to 'l1.pop(1)', since 96 on our list was now on index 1...