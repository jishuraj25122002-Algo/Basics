# ---------------------------------------------------------
# Program: Print 1 to N Using Recursion
# ---------------------------------------------------------

def print_numbers(n):
    """Print numbers from 1 to n using recursion."""

    # Base case
    if n == 0:
        return

    # Recursive call
    print_numbers(n - 1)

    # Print after recursive call
    print(n)


# ---------------------------------------------------------
# Driver Code
# ---------------------------------------------------------

n = int(input("Enter the value of n: "))

print(f"\nNumbers from 1 to {n}:")

print_numbers(n)