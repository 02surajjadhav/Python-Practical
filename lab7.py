text = input("Enter a paragraph: ")

words = len(text.split())

vowels = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1

spaces = text.count(" ")

characters = len(text)

print("\n--- Text Analysis ---")
print("Words      :", words)
print("Vowels     :", vowels)
print("Spaces     :", spaces)
print("Characters :", characters)