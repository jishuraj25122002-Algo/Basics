print("printing current and previous number sum in a range (10): " )
previous=0
for i in range(10):
  current = i 
  sum=previous+current
  previous=current -1
  print(f"Current number :{i} and previous number :{previous} and sum : {previous + current }")