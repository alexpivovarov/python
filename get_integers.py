'''
Create a Python function named "get_integers" that accepts a list of mixed non-negative integers and strings.
The function should filter and return only the integers in the same order as they appear in the original list.
'''

def get_integers(mixed_list):
    new_list = []
    for item in mixed_list:
        if isinstance(item, int): # Check if the item is an integer
            new_list.append(item)
    return new_list


user_input = input("Enter a list of non-negative integers and strings separated by commas e.g. two, 5, 6, zero : ")
mixed_list = []
for item in user_input.split(','): #split a string into a list of substrings based on a specified delimiter, which in this case is a comma (,).
    item = item.strip() # Removing any surrounding whitespace
    if item.isdigit(): # Checking that item is an integer
        mixed_list.append(int(item)) # Converting numeric strings to integers
    else:
        mixed_list.append(item) # Leave non-numeric strings as they are

print(f"The list of integers from the mixed list is {get_integers(mixed_list)}")