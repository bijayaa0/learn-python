# Implement a program to print Fibonacci series up to $n$ terms using while and else.
num = int(input("Enter the total series: "))

a = 0
b = 1
count = 0

while count < num:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
else:
    print("\nSeries completed.")
