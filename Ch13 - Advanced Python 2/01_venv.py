# Ch13 - Advanced Python 2 - Right click - Open with VSCode.

# in terminal:
# pip install virtualenv

#then,
# virtualenv env

# In Ch13 - Advanced Python 2 Folder, do right click and open with terminal.
# In terminal, Enter - pip install pandas==1.5.2
# This installs pandas version 1.5.2 globally.

# Suppose if i want to work with a lower verison of pandas
# Say, 1.5.1, and i don't want to globally install 1.5.1
# (Installing 1.5.1 globally will first remove the already installed 1.5.2)

# In that case, I can work in a virtual environment.

# Virtual Environment: An environment which is same as the system interpreter but is isolated from the other Python environments on the system.

# Let's activate this virtual environment:

# In the same terminal (opened in the folder containing 'env' sub folder),

# Enter:  .\env\Scripts\activate.ps1    (Enter 'env' and use 'tab' key)

# Now you'll see '(env)', indicating that virtual environment is activated.

# Now I can do pip install pandas==1.5.1 to install pandas version 1.5.1 in that virtual environment and work with it.
# but globally on my pc, the pandas version 1.5.2 remains installed.

# Note that this '(env)' might not be shown in VSCode, but since we did 'venv' we are in virtual env already.

# To exit from virtual environment, in the same terminal,
# Enter: deactivate

# ---------------------------------

