'''
Given a list, write a Python program to swap first and last element of the list.

Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''

def swap(user_list):
    first_element = user_list[0]
    last_element = user_list[-1]

    user_list[0] = last_element
    user_list[-1] = first_element

    return(user_list)

user_input = input("Enter a list: ")
user_list = user_input.split(",") # Splitting the input string by commas to create a list of strings

swapped_list = swap(user_list)

print(f"The new list is {swapped_list}")
