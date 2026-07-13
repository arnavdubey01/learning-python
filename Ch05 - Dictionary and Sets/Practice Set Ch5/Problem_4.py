# What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20') 

print(s, len(s))

#Length of s comes out to be 2.
#Because, python sees integer '20' and floating point '20.0' as same.

print(20 == 20.0)   #Python returns 'True'

#Basically, two values are same, then datatype(integer/floating point) doesn't matter.

