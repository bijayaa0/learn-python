# Create a script that takes a list of numbers and prints "Prime" for each prime number and "Not Prime" for others.

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
for num in numbers:
    if num <= 1:
        print(num, "Not Prime")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "Not Prime")
                break
        else:
            print(num, "Prime")
