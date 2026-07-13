# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

#Set does not have indexing, so no.
#Also, we see a list '[1,2]' in the set s, which can not be there either.
#So, you can not even create this set in first place because of the list.
 
#---------------------------------------------------------------

#ChatGPT explaination:
# No, you cannot even create this set in the first place, so the question becomes invalid.

# Why?

# Sets in Python can only contain hashable (immutable) elements.
# A list is mutable, so it is unhashable → it cannot be added to a set.
# s = {8, 7, 12, "Harry", [1,2]}
# This will raise:
# TypeError: unhashable type: 'list'

# So:
# You cannot include a list inside a set
# Therefore, you cannot change values inside such a list
# What if you did want something similar?

# You could use a tuple instead of a list (since tuples are immutable and hashable):

# s = {8, 7, 12, "Harry", (1,2)}

# But then:

# You still cannot change values inside the tuple, because tuples are immutable.
# Final takeaway:
# ❌ List in set → not allowed
# ❌ Modifying elements inside set → not allowed
#** ✅ Only immutable elements (int, str, tuple, etc.) are allowed in sets

#-------------------------------------------------------------------

#Basically, answer is no.