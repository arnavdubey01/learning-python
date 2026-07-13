# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

l = [111, 232, 34, 44, 839, 393, 786, 22]

def greatest(a, b):
    if(a>b):
        return a
    return b

print(reduce(greatest, l))

# basically 
# 111, 232, 34, 44, 839, 393, 786, 22
#   \  /
#    232  , 34, 44, 839, 393, 786, 22
#       \   /
#        232  , 44, 839, 393, 786, 22
#           \   /
#            232  , 839, 393, 786, 22
#               \   /
#                839   , 393, 786, 22
#                   \   /
#                    839    , 786, 22
#                       \    /
#                         839    , 22
#                            \    /
#                              839      #output

# So this is how it works:

# l = [111, 232, 34, 44, 839, 393, 786, 22]
# it first compares first two elements (111 and 232), accoridng to 'greatest()'
# since 232 is graeater, now it compares 232 and 34, 232 greater again
# now it compares 232 and 44, 232 greater again
# now it compares 232 and 839, 839 is greater, so:
# now it compares 839 and 393, 839 is greater
# now it compares 839 and 786, 839 is greater again
# now it compares 839 and 22, 839 is greater.

# So prints output as 839.