#Write a program to check how many times a character is repeated in a word?
word = input("Enter a word: ")
char = input("Enter a character: ")
count = 0
for i in word:
    if i == char:
        count += 1
print(f"The character '{char}' appears {count} times in the word '{word}'.")