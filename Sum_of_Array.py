# ---------------------------------------------------------
# Program: Sum of Array Elements Using Recursion
# ---------------------------------------------------------

def array_sum(arr, n):
    """
    Recursively calculates the sum of array elements.

    Parameters:
        arr : List of numbers
        n   : Number of elements to consider

    Returns:
        Sum of the array elements
    """

    # Base case: No elements left
    if n == 0:
        return 0

    # Recursive case
    return arr[n - 1] + array_sum(arr, n - 1)


# ---------------------------------------------------------
# Driver Code
# ---------------------------------------------------------

# Take array elements from the user
arr = list(map(int, input("Enter array elements: ").split()))

# Calculate the sum using recursion
result = array_sum(arr, len(arr))

# Display the result
print("\nArray:", arr)
print("Sum of array elements:", result)