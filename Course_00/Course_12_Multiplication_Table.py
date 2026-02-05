# 12.Generate a multiplication table for a given number using a for loop.
print("Multiplication Table.")
num = int(input("Enter a number:"))
print(f"The multiple of {num}:")
for i in range(1,11,1):
    print(f"{num} x {i} = {num*i}")
