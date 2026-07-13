# Write a program to mine a log file and find out whether it contains word 'python'.

#made log.txt file, then selected language model sa HTML (Bottom right corner)
#typed "lorem435" and pressed enter, it printed long text.

with open("log.txt") as f:
    content=f.read()

if ("python" in content):
    print("Yes, the word \"python\" is in the content")
else:
    print("No, the word \"python\" is not present")
    