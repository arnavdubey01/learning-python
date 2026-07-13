st = "\"This is appended line from 04_append.py\""

f = open("file.txt", "a")   #"a" is for 'append'

f.write(st)
f.close

