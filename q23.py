def check_palindrome(number):
    # Convert to string to easily reverse
    str_num = str(number)
    reverse_str = str_num[::-1]
    
    if str_num == reverse_str:
        print(f"Original number {number}")
        print("Yes. given number is palindrome number")
    else:
        print(f"Original number {number}")
        print("No. given number is not palindrome number")

check_palindrome(121)