#Write a script to determine if a string is a palindrome.

text = input("Enter a string: ").lower().replace(" ","")

rev_text = text[::-1]
print("Your string: ",text)
print("Reversed string: ",rev_text)
if(text == rev_text):
    print("palindrome.")
else:
    print("not palindrome.")
