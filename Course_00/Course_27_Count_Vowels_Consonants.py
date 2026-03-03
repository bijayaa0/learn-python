# Develop a function that takes a string and counts the number of vowels and consonants using for loop and if statements.

def counter(in_str):
    v_list = ["a", "e", "i", "o", "u"]
    v_count = 0
    c_count = 0

    for x in in_str.lower():
        if x.isalpha():  # only count letters
            if x in v_list:
                v_count += 1
            else:
                c_count += 1

    print(f"Vowels: {v_count} and Consonants: {c_count}")

in_str = input("Enter a string: ")
counter(in_str)
