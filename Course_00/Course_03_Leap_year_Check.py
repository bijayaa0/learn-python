#Create a function that takes a year as input and checks if it is a leap year.

year = int(input("Enter the year: "))
if(year % 4 == 0 and year % 100 != 0):
    print(year,"is a leap year.")
elif(year % 400 == 0 ):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")

