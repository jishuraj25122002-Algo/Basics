text = "hello world from python"

# Split the string into a list of words
words = text.split()
capitalized_words = []

for word in words:
    # Capitalize each word and add to the new list
    capitalized_words.append(word.capitalize())

# Join the list back into a single string
result = " ".join(capitalized_words)
print(result)