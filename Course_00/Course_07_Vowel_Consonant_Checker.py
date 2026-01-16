#Write a program to check if a given character is a vowel or consonant.
ch = input("Enter a character: ").lower()

if ch in ('a', 'e', 'i', 'o', 'u'):
    print("Vowel")
else:
    print("Consonant")

