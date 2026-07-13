#Check that tuple type can not be changed in python.

a = (32, 232,"Hello")

a[2] = "Larry"
print(a)
#This shows error

#But if we used box brackets '[...]', then it would be interpreted as list, so it would give a valid output.