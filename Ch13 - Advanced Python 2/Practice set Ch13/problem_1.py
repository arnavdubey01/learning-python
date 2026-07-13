# 1. Create two virtual environments, install few packages in the first one. 
# How do you create a similar environment in the second one?

# In explorer, folder 'Practice set Ch13', do right click and open in terminal.

# Now enter: virtualenv env1
# Then enter: virtualenv env2

# Now the two virtual environments are created.
# .\env1\Scripts\activate.ps1        #Activated env1
# pip install pandas
# pip install pyjokes
# pip freeze > requirements.txt     #requirements.txt file is created.


# Now, activate the second virtual environment, but first, deactivate env1:

# deactivate                        #Deactivated env1
# .\env2\Scripts\activate.ps1       #Activated env2
# pip install -r requirememts.txt   #all packages from env1 are installed in env2