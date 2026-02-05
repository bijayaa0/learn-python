# 15.Write a program to print all the prime numbers within a given range.
range_num = int(input("Enter the range: "))
for i in range (2,range_num):
    is_prime = True
    for j in range(2, i):
        if  i % j == 0:
            is_prime = False
            break
    if is_prime:
            print(i)

