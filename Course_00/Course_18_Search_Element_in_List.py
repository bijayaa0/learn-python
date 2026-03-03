# Write a program that searches for an element in a list and stops the search once the element is found using break.

num = int(input("Enter the total element in list: "))
l_num = []

for x in range(1, num + 1):
    l_num.append(int(input(f"Element {x}: ")))

print(f"Your list {l_num}")

f_num = int(input("Find element: "))

for x in l_num:
    if f_num == x:
        print(f"Element {f_num} is found.")
        break
else:
    print("Element not found.")
