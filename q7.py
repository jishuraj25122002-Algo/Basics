#driver code
arr=[]
n=int(input("Enter the number of elements in the array :"))
for i in range(n):
  element=int(input(f"Enter element {i+1} :"))
  arr.append(element)
print(f"Array : {arr}")
a=int(input("Enter the element to delete from the array :"))
arr.remove(a)
print(f"Array after deleting {a} : {arr}")