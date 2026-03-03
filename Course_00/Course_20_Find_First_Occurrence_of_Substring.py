# Create a script to find the first occurrence of a substring in a string using for and break.
main_str = input("Enter main string: ")
sub_str = input("Enter substring: ")

for i in range(len(main_str) - len(sub_str) + 1):
    if main_str[i:i+len(sub_str)] == sub_str:
        print(f"First occurrence at index {i}")
        break
else:
    print("Substring not found")
