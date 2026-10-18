rows = 5
# Outer loop for number of rows
for i in range(rows, 0, -1):
    # Inner loop for printing numbers in each row
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("") # New line

    