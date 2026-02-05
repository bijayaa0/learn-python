# 11. Write a program to sum all the items in a list.
num = [1,2,3,"ram",3.5,"sita",1]
sum = 0
for i in num:
    if isinstance(i,(int,float)):
        sum += i
print(f"List data = {num}")
print(f"The sum of list = {sum}")
