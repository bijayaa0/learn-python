print("Enter two numbers:")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print("Operations: addition, subtraction, multiplication, division")
opr = input("Enter any operation: ").lower().replace(" ", "")

if opr == "addition":
    print(f"The addition of {num1} and {num2} is {num1 + num2}")

elif opr == "subtraction":
    print(f"The subtraction of {num1} and {num2} is {num1 - num2}")

elif opr == "multiplication":
    print(f"The multiplication of {num1} and {num2} is {num1 * num2}")

elif opr == "division":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        print(f"The division of {num1} and {num2} is {num1 / num2}")

else:
    print("Invalid input.")
