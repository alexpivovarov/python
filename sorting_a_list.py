'''
 Sort a List

Write a Python function that takes two parameters: a list of numbers and a second parameter that can have one of three
values: "asc", "desc", or "none".

If the second parameter is "asc", the function should return the list of numbers in ascending order. If it is "desc",
the function should return the list of numbers in descending order. If the second parameter is "none", the function
should return the unaltered list.
'''


def sorter(user_list, user_choice):
    if user_choice == 'desc':
        user_list.sort(reverse=True)
    elif user_choice == 'asc':
        user_list.sort()
    elif user_choice == 'none':
        pass
    else:
        return "Invalid input"
    return user_list


user_input = input("Enter a list in format [a, b, c, d ... ] where a, b, c, d are numbers: ")

# Converting the input string to a list of numbers
user_list = user_input.strip('[]') # Removing the square brackets
user_list = user_list.split(',') # Split the string into individual elements
user_list = [float(i) for i in user_list] # Convert each element to a float


user_choice = input("Type 'desc' if list should be ordered in the descending order, 'asc' in ascending order and 'none' for no change: ")


sorted_list = sorter(user_list, user_choice)
print(sorted_list)