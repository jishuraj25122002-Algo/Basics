#method implementation
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)

#driver code
n=int(input("Enter a integer number : "))
result=factorial(n)
print(f"factorial of {n} is :{result }")