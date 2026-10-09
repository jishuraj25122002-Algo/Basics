number=[]
n=int(input("Enter the number of elements in the list : "))
for i in range(n):
  element=int(input("Enter the element : "))
  number.append(element)
maximum=max(number)
print("The maximum element in the list is :", maximum)
minimum=min(number)
print("The minimum element in the list is :", minimum)