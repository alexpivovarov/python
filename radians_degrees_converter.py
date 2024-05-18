import math

user_choice = input("Enter 'rd' if you would like to change radians into degrees or 'dr' if you would like to change degrees into radians: ")

value = float(input("Enter a value to convert: "))

if user_choice == "rd":
    converted_value = math.degrees(value)
    print(f"{value} radians is equal to {converted_value} degrees")
elif user_choice == "dr":
    converted_value = math.radians(value)
    print(f"{value} degrees is equal to {converted_value} radians")
else:
    print("Invalid input")



