f = open("file.txt")

lines = f.readlines()       #This prints all lines as a list.
print(lines, type(lines))
#----------------------------------------------------------------------
#readlines() and readline() are different commands
#In readline(), a single line is printed as a string.
line1= f.readline()       
print(line1, type(line1))

line2= f.readline()        #Same command is run again, now it prints the next line 
print(line2, type(line2))

line3= f.readline()         #Same command run third time, so third line is printed
print(line3, type(line3))   

line4= f.readline()         #Same command run fourth time, so fourth line is printed
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))   #Nothing gets printed, because line 5 does not exist in out file.txt
#so,
line5 = f.readline()
print(line5 == "")      #Returns 'true', meaning it is an empty string. 

#To do the above thing, we can also use while loop.

line = f.readline()
while(line != ""):      # '!=' means "not equal to"
    print(line)
    line = f.readline()

f.close()