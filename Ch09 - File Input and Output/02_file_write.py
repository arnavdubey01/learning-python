f = open("myfile.txt", "w") #"w" tells python to open file in write mode, by default, it opens file in read mode.

st = ('''Fun Fact: Guido van Rossum named the Python programming language
after the British comedy troupe Monty Python's Flying Circus—not the snake. 
It is a versatile, high-level language that powers modern tech from AI and
machine learning to NASA data analysis.
''')


f.write(st)
f.close()


#A new "myfile.txt" file was created by python, and 'st' was written in it.