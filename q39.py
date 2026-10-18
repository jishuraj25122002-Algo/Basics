try:
  with open("notes.txt","r") as file:
    data=file.read()
    content=data.split()
    words=len(content)
    print(f"the file contains {words} words . ")
except FileNotFoundError:    
  print("Error !! this file is not found ")