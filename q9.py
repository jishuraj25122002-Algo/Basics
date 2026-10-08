word=str(input("Enter a string : "))
vowel="aeiou"
count = 0
for i in word.lower():
  if i in vowel:
    count+=1
print(f"The number of vowels in the string is : {count}")    