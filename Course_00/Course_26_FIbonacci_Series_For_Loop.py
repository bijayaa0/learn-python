# Write a Python program to print the first n Fibonacci numbers using a for loop.

num = int(input("Enter total number series: "))
a = 0
b = 1
for x in range(num):
    print (a,end=" ")
    c = a + b

    a = b
    b = c
else:
    print("Series completed")
