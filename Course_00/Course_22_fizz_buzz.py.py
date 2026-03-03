# Write a Python program that takes a list of integers and prints "Fizz" for multiples of 3,"Buzz" for multiples of 5, 
# and "FizzBuzz" for multiples of both 3 and 5.

num = int(input("Enter the total element in list: "))
l_num = []

for x in range(1, num + 1):
    l_num.append(int(input(f"Element {x}: ")))

print(f"Your list {l_num}")
for x in l_num:
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("FzzBuzz")
    else:
        print(f"{x} is not multiple of 3 and 5.")
    
