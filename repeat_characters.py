'''
Create a function that accepts strings. The function thus created should be able to return a string where each character
is doubled in the original string.
'''

def double(string):
    new_string = "" # Initialising an empty string
    for char in string:
        new_string += char * 2 # Appending the character twice to the new string
    return new_string

string = input("Enter a string: ")
print(f"The new string is {double(string)}")