num = int(input("Enter the size of list: "))

lst = []
for i in range(num):
    lst.append(int(input()))

print(f"Your list : {lst}")

large = max(lst)
print(f"Largest number : {large}")
