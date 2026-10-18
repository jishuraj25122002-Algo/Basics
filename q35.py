user_input = "Python3"
contains_digit = False

# Iterate through each character
for char in user_input:
    if char.isdigit():
        contains_digit = True
        break  # Exit early since we found one

print(f"The string '{user_input}' contains digits: {contains_digit}")