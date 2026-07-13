n: int = 5
name: str = "Harry"

def sum(a: int, b: int) -> int:
    return (a+b)

# Type hints are added using the colon ' : ' syntax for variables and ' -> ' syntax for function return types.

# This makes it easy for someone else looking at the code to know the variable's type of data set. 

# Basically, tells the type of function, that's it. 
# There won't be any difference in output if someone doesn't use ' : ' or ' -> '

# We also have advanced type hints:

from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union type
identifier: Union[int, str] = "ID123"

# # Basically, makes it easy to identify the data structrues by looking at the code, that's it. It also makes code self-documenting