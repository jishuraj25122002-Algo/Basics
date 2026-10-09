number=[]
n=int(input("Enter the number of elements in the list : "))
for i in range(n):
  element = int(input(f"Enter the element {i+1} : "))
  number.append(element)
result=set(number)
print("The unique elements in the list are :", result)