with open("notes.txt","w") as file:
  file.write("Hi my name is jishraj maity and my mother name is madhuri maity \n")
  file.write("and my father name is goutam kumar maity \n")
  file.write("my sister name is puja maity ")
with open("notes.txt","r") as file:
  content = file.read()  
  print(content)