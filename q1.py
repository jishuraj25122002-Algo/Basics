def multiplication(n1,n2):
  mul=n1*n2
  if mul <=1000:
    return mul
  else:
    return (n1+n2)

n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
result=multiplication(n1,n2)
print(result )