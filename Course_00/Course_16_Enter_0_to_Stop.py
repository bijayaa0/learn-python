# Write a program that asks the user to enter a number and stops when the user enters 0 using a while loop.
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break

print("Program stopped.")
