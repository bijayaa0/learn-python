
def fact(num):
    i = 1
    while num > 0:
        i *= num
        num-=1
    return i
print("Calculating factorial:")
num = int(input("Enter a number: "))
print(f"The factorial of {num} : {fact(num)}")
