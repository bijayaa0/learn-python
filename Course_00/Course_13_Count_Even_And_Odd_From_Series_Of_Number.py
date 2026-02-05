# 13.Write a script to count the number of even and odd numbers from a series of numbers.
num = int(input("How many numbers: "))
num_list = []
print("Enter the series of numbers: ")
for i in range(num):
    num_in = int(input("Number: "))
    num_list.append(num_in)

count_even = 0
count_odd = 0
for i in num_list:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd +=1

print(f"The series of number : {num_list}")
print(f"The total even numbers from the series of numbers : {count_even}")
print(f"The total odd numbers from the series of numbers : {count_odd}")
