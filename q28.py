numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
evens = []
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")