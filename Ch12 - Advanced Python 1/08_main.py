# See module.py

from module import myFunc   

# Note that the name of module should be no other than module.

# Here, __name__ is printed as 'module'.


# # '__name__' evaluates to the name of the module in python from where the program is ran.
# If the module is being run directly from the command line, the '__name__' is set to string "__main__".
# Thus, this behaviour is used to check whether the module is run directly or imported to another file