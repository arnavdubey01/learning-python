s = {1, 2, 3, 3, 3}  #Basically, Class 11 Maths chapter 1 - Sets.

#Since e = {} was empty dictionary, to make empty set, we do:
e = set() # - This is an empty set
#So, e = {} will create an empty dictionary, not an empty set.  - Asked in interviews.

print(s) # - This prints {1, 2, 3}, but, isn't s = {1, 2, 3, 3, 3}?
#Remember Class 11 Maths Ch1, elements can not repeat in set.  

#So, we use sets when we have use case in which we don't want elements to repeat themselves.
#Also note, that order is not maintained in sets, to maintain order, use list.


# Sets are unordered => Element’s order doesn’t matter
# Sets are unindexed => Cannot access elements by index
# There is no way to change items in sets.
# Sets cannot contain duplicate values.
