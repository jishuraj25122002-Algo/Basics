#method implementation
def merge(list1,list2):
  result_list=[]

  for num in list1:
    if num % 2 != 0 :
      result_list.append(num)

  for i in list2:
    if i % 2 == 0:
      result_list.append(i)

  return result_list        

#driver code
list1=[ int(x) for x in input("Enter the elements separated by space : ").split()]
list2=[ int(x) for x in input("Enter the elements separated by space : ").split()]
result=merge(list1,list2)
print(result)