# Write a program that reads a list of strings and prints only the strings that start with a vowel.

words = input("Enter words separated by space: ").split()
vowels = "aeiou"

for word in words:
    if word[0].lower() in vowels:
        print(word)
