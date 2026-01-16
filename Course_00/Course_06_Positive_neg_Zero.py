#Create a function that categorizes an integer as positive, negative, or zero.
def checker(num):
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")

num = int(input("Enter a number: "))
checker(num)
