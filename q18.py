# arr = [ int(x) for x in input("Enter the elements seperated by space : ").split()]
num=int(input("Enter a number : "))

while num !=0 :
  rem=num%10
  num = num // 10 
  print(rem , end = " ")