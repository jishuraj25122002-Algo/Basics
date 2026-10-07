#method implementation
def remove_chars(word,n):
  new_word=list(word[n:])
  return ''.join(new_word)  

#driver code
word=str(input("Enter a string : "))
n=int(input("Enter a number upto n to return new string : "))
result=remove_chars(word,n)
print(result)