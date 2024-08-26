def is_binary(s):
    return all(char in '01' for char in s) # Checking if the string "s" is a valid binary number

def binary_to_decimal(binary_str):
    return int(binary_str, 2) # Converting a binary string to a decimal number

def decimal_to_binary(decimal_number):
    return bin(decimal_number).replace("Ob", "") # converts a decimal number to its binary string representation and then removes the '0b' prefix that Python includes by default.


user_choice = input("Type 'd-b' if you would like decimal number to be converted into binary number and type 'b-d' if you would like binary number to be converted into decimal number: ")
user_number = input("Enter the number to be converted: ").strip() # new string is returned with whitespace at the beginning or end removed


if user_choice == 'd-b':
    if user_number.isdigit(): # checking whether the string user_number consists entirely of digits
        decimal_number = int(user_number) # converting the string into integer
        binary_result = decimal_to_binary(decimal_number) # converting decimal into binary
        print(f"The binary representation of {decimal_number} is {binary_result}")
    else:
        print("Invalid input. Please enter a valid decimal number.")
elif user_choice == "b-d":
    if is_binary(user_number): # checking whether user_binary consists of "1"s and "0"s and converting binary string into integer.
        decimal_result = binary_to_decimal(user_number) # converting binary into decimal
        print(f"The decimal representation of {user_number} is {decimal_result}")
    else:
        print("Invalid input. Enter a valid binary number.")
else:
    print("Invalid choice. Please type 'd-b' for decimal to binary and 'b-d' for binary to decimal.")

