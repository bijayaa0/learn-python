# Create a script that finds and prints all Armstrong numbers in a given range using nested loops.

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    temp = num
    total = 0

    # Count digits
    digits = len(str(num))

    # Inner loop to calculate sum of powers
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    if total == num:
        print(num, "is an Armstrong number")
