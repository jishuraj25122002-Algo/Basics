def check_palindrome(number):
    print("original number", number)
    # Convert to string to reverse easily
    original_str = str(number)
    reversed_str = original_str[::-1]
    
    if original_str == reversed_str:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")

check_palindrome(121)
check_palindrome(125)