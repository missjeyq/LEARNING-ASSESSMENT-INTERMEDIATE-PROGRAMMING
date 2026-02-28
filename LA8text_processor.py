print("Text Processor Program")

sentence = input("Enter a sentence: ")

print("\n === Case Transformations ===")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title Case:", sentence.title())

count_a = sentence.lower().count('a')
print("Number of 'a' letter in sentence:", count_a)

trimmed = sentence.strip()
print("\nWithout leading/trailing spaces:")
print(trimmed)

underscore = sentence.replace(" ","_")
print("\nSpaces replaced undercore:")
print(underscore)

print("\nWords in the sentence:")
words = sentence.split()

for word in words:
    print(word)